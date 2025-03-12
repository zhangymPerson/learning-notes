#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@file : py_compare.py
@desc : 脚本运行方式 [python3 py_compare.py]
        脚本说明: 比较两个文件夹下所有文件的内容差异
@date : 2025-03-12 18:39:54
@auth : danao
@version : 1.0
"""

import os
import difflib
import argparse
import yaml
from pathlib import Path

DEFAULT_IGNORE_FILE = ".fileignore.yaml"


def load_ignore_patterns(config_path=None):
    """
    加载忽略模式配置
    返回结构：{'prefixes': [], 'suffixes': []}
    """
    default_patterns = {'prefixes': [], 'suffixes': []}

    # 查找配置文件路径
    config_locations = [
        config_path,
        Path.cwd() / DEFAULT_IGNORE_FILE,
        Path(__file__).parent / DEFAULT_IGNORE_FILE
    ]

    for loc in config_locations:
        if loc and loc.exists():
            try:
                with open(loc, 'r') as f:
                    config = yaml.safe_load(f)
                    # 验证配置格式
                    if isinstance(config, dict) and 'ignore' in config:
                        return {
                            'prefixes': config['ignore'].get('prefixes', []),
                            'suffixes': config['ignore'].get('suffixes', [])
                        }
                    print(f"警告：配置文件格式错误 {loc}")
            except Exception as e:
                print(f"加载配置文件错误 {loc}: {str(e)}")
            break

    print("使用默认忽略配置（无规则）")
    return default_patterns


def should_ignore(filename, patterns):
    """判断文件是否应被忽略"""
    # 检查前缀匹配
    if any(filename.startswith(p) for p in patterns['prefixes']):
        return True
    # 检查后缀匹配（支持完整扩展名匹配）
    if any(filename.endswith(p) for p in patterns['suffixes']):
        return True
    return False


def get_files_dict(dir_path, ignore_patterns):
    """获取目录下文件的相对路径字典（带过滤）"""
    file_dict = {}
    for root, dirs, files in os.walk(dir_path):
        # 先过滤文件再处理
        filtered_files = [
            f for f in files
            if not should_ignore(f, ignore_patterns)
        ]

        for file in filtered_files:
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, dir_path)
            file_dict[rel_path] = abs_path
    return file_dict


def compare_directories(dir1, dir2, ignore_patterns):
    """比较两个目录并返回差异文件列表"""
    dir1_files = get_files_dict(dir1, ignore_patterns)
    dir2_files = get_files_dict(dir2, ignore_patterns)

    common_files = set(dir1_files.keys()) & set(dir2_files.keys())
    if not common_files:
        return []

    diff_files = []
    for rel_path in common_files:
        file1 = dir1_files[rel_path]
        file2 = dir2_files[rel_path]
        if not is_file_content_equal(file1, file2):
            diff_files.append(rel_path)

    return diff_files


def is_file_content_equal(file1, file2):
    """比较两个文件内容是否完全相同（二进制安全版）"""
    if os.path.getsize(file1) != os.path.getsize(file2):
        return False

    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        while True:
            b1 = f1.read(4096)
            b2 = f2.read(4096)
            if b1 != b2:
                return False
            if not b1:
                return True


def show_diff(file1, file2):
    """显示两个文件的差异对比（增强版）"""
    try:
        with open(file1, 'r', encoding='utf-8') as f1:
            lines1 = f1.readlines()
    except UnicodeDecodeError:
        return "⚠️ 文件无法用UTF-8解码，可能不是文本文件"

    try:
        with open(file2, 'r', encoding='utf-8') as f2:
            lines2 = f2.readlines()
    except UnicodeDecodeError:
        return "⚠️ 文件无法用UTF-8解码，可能不是文本文件"

    diff = difflib.unified_diff(
        lines1, lines2,
        fromfile=os.path.abspath(file1),
        tofile=os.path.abspath(file2),
        lineterm='',
        n=3  # 显示上下文3行
    )
    return '\n'.join(diff)


def setup_args_parser():
    """配置命令行参数解析器"""
    parser = argparse.ArgumentParser(
        description='目录文件差异比较工具',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog='使用示例:\n'
               '  python diff_tool.py -o old_dir/ -n new_dir/\n'
               '  python diff_tool.py --old-dir v1.0/ --new-dir v2.0/'
    )
    parser.add_argument('-o', '--old-dir',
                        required=True,
                        help='原始目录路径（旧版本）',
                        metavar='PATH')
    parser.add_argument('-n', '--new-dir',
                        required=True,
                        help='新目录路径（新版本）',
                        metavar='PATH')
    parser.add_argument('-c', '--config',
                        help=f'指定配置文件路径（默认查找 {DEFAULT_IGNORE_FILE}）',
                        metavar='FILE')
    return parser


def main():
    # 解析命令行参数
    parser = setup_args_parser()
    args = parser.parse_args()

    # 标准化路径处理
    old_dir = os.path.normpath(args.old_dir)
    new_dir = os.path.normpath(args.new_dir)

    # 验证目录有效性
    if not os.path.isdir(old_dir):
        print(f"错误：旧目录不存在 {old_dir}")
        return
    if not os.path.isdir(new_dir):
        print(f"错误：新目录不存在 {new_dir}")
        return
    # 加载忽略规则
    ignore_patterns = load_ignore_patterns(args.config)
    print(
        f"当前忽略规则：前缀 {ignore_patterns['prefixes']}，后缀 {ignore_patterns['suffixes']}")

    # 比较目录
    diff_files = compare_directories(old_dir, new_dir, ignore_patterns)

    if not diff_files:
        print("\n✅ 所有同名文件内容一致")
        return

    # 显示差异文件列表
    print(f"\n🔍 发现 {len(diff_files)} 个差异文件：")
    for idx, file in enumerate(diff_files, 1):
        print(f"[{idx:02d}] {file}")

    # 交互式查看差异
    while True:
        choice = input("\n输入要查看的文件序号 (q退出/r刷新列表)：").strip().lower()
        if choice == 'q':
            break
        if choice == 'r':
            diff_files = compare_directories(old_dir, new_dir, ignore_patterns)
            print("\n已刷新差异文件列表：")
            for idx, file in enumerate(diff_files, 1):
                print(f"[{idx:02d}] {file}")
            continue

        if not choice.isdigit():
            print("错误：请输入有效数字")
            continue

        index = int(choice) - 1
        if 0 <= index < len(diff_files):
            rel_path = diff_files[index]
            file_old = os.path.join(old_dir, rel_path)
            file_new = os.path.join(new_dir, rel_path)
            print(f"\n📝 差异对比 {rel_path}:")
            print(show_diff(file_old, file_new))
        else:
            print(f"错误：无效序号，请输入 1-{len(diff_files)} 之间的数字")


if __name__ == "__main__":
    main()
