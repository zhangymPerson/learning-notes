# UV (Python 管理器) 备忘录

## 安装与卸载

1. **安装**

   ```bash
   pip install uv
   ```

2. **升级**

   ```bash
   pip install --upgrade uv
   ```

3. **卸载**
   ```bash
   pip uninstall uv
   ```

---

## 项目管理

1. **创建新项目**

   ```bash
   uv new <project_name>  # 创建项目目录和基础结构
   cd <project_name>
   ```

2. **初始化虚拟环境**
   ```bash
   uv venv  # 默认在项目根目录创建 `.venv` 环境
   ```

---

## 依赖管理

1. **安装依赖包**

   ```bash
   uv install <package_name>          # 安装单个包
   uv install -r requirements.txt     # 从文件批量安装
   ```

2. **卸载依赖包**

   ```bash
   uv uninstall <package_name>
   ```

3. **生成依赖清单**
   ```bash
   uv freeze > requirements.txt  # 导出当前环境依赖
   ```

---

## 环境管理

1. **切换 Python 版本**

   ```bash
   uv python --version 3.11  # 指定 Python 版本（需已安装）
   ```

2. **激活虚拟环境**

   ```bash
   source .venv/bin/activate  # Linux/macOS
   .\.venv\Scripts\activate   # Windows
   ```

3. **退出虚拟环境**
   ```bash
   deactivate
   ```

---

## 常用命令速查

| 功能             | 命令             |
| ---------------- | ---------------- |
| 查看已安装包列表 | `uv list`        |
| 检查环境状态     | `uv status`      |
| 清理缓存         | `uv cache clean` |
| 查看版本信息     | `uv --version`   |

---

## 备注

1. 通过 `uv config` 可配置镜像源（如切换至阿里云/清华源）
2. 使用 `uv venv --name <env_name>` 可创建多环境
3. 建议在项目根目录操作以自动识别虚拟环境
