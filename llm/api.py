# 请安装 OpenAI SDK : pip install openai
# apiKey 获取地址： https://console.bce.baidu.com/iam/#/iam/apikey/list
# 支持的模型列表： https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Fm2vrveyu
import time
from openai import OpenAI
import readline

# sqlite 读写库
import sqlite3
import os


def create_ai_history_table(db_path: str):
    """
    创建历史记录表
    1. 判断数据库文件是否存在，不存在则创建
    2. 判断表是否存在，不存在则创建
    :param db_path: 数据库路径
    """
    if not os.path.exists(os.path.dirname(db_path)):
        os.makedirs(os.path.dirname(db_path))

    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        # 创建表
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ai_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_input TEXT NOT NULL,
                ai_response TEXT NOT NULL,
                time_cost REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        # 提交事务
        conn.commit()
    except sqlite3.Error as e:
        print(f"创建表失败: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()


def insert_message_info(
    dbpath: str, id: int, question: str, answer: str, time_cost: float
):
    """
    写入历史记录表并返回插入的id
    判断 id 是否存在，如果存在则更新，如果不存在则插入
    :param dbpath: 数据库路径
    :param id: 用户输入的id
    :param question: 用户输入的question
    :param answer: AI的回答
    :param time_cost: 耗时
    """
    conn = None
    try:
        conn = sqlite3.connect(dbpath)
        cursor = conn.cursor()
        # id 是否为空或者0
        if id is None or id == 0:
            # 插入数据
            cursor.execute(
                """
                INSERT INTO ai_history (user_input, ai_response, time_cost)
                VALUES (?, ?, ?)
            """,
                (question, answer, time_cost),
            )
            # 提交事务
            conn.commit()
            # 获取插入数据的 id
            id = cursor.lastrowid
        else:
            # 更新数据
            cursor.execute(
                """
                UPDATE ai_history SET user_input = ?, ai_response = ?, time_cost = ? WHERE id = ?
            """,
                (question, answer, time_cost, id),
            )
            conn.commit()
    except sqlite3.Error as e:
        print(f"插入数据失败: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
    return id


def send_message_api(message: str):
    client = OpenAI(
        base_url="https://qianfan.baidubce.com/v2",
        api_key="百度云获取的apiKey",
    )
    chat_completion = client.chat.completions.create(
        # 模型名称 可以去百度模型列表查看
        model="deepseek-r1",
        messages=[{"role": "user", "content": f"{message}"}],
    )
    # 解析 chat_completion 中的 message 中的 content
    content = chat_completion.choices[0].message.content
    return content


def send_message_api_stream(message: str):
    client = OpenAI(
        base_url="https://qianfan.baidubce.com/v2",
        api_key="百度云获取的apiKey",
    )
    stream = client.chat.completions.create(
        # 模型名称 可以去百度模型列表查看
        model="deepseek-r1",
        messages=[{"role": "user", "content": f"{message}"}],
        stream=True,
        temperature=0.3,
        max_tokens=1000,
    )
    content = ""
    for chunk in stream:
        # 试试输出流式响应并合并到content
        if chunk.choices[0].delta.content is not None:
            content += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="", flush=True)
    return content


def main():
    """
    主要是处理
    """
    print("ai 问答小工具")
    print("输入 list 查看历史记录")
    print("输入 exit 或者 quit 退出")
    dbpath = "/home/dev/.script/ai_history.db"
    create_ai_history_table(dbpath)
    # 循环获取用户输入内容，直到用户输入 exit 或者 quit
    while True:
        message = input("请输入要发送的消息(输入 exit 或者 quit 退出)：")
        message = message.strip()
        if message == "list":
            conn = sqlite3.connect(dbpath)
            cursor = conn.cursor()
            row = input("请输入查询条数：")
            if not row.isdigit() or int(row) > 1000:
                print("请输入小于1000的数字")
                row = 10
            cursor.execute(
                "SELECT * FROM ai_history order by created_at desc limit ? ", (
                    row,)
            )
            rows = cursor.fetchall()
            for row in rows:
                line = "==================================================================================="
                print(line)
                print(f"提问时间:{row[4]},耗时:{row[3]}s")
                print(f"用户提问:{row[1]}")
                print(f"AI 回复：{row[2]}")
                print(line)
            continue
        if message == "" or message == "exit" or message == "quit":
            break
        # 发送的消息是 message
        # 计算耗时
        start_time = time.time()
        print(f"用户输入：{message}")
        id = insert_message_info(dbpath, 0, message, "", 0)
        try:
            # 使用流式输出，避免响应等待时间过长
            content = send_message_api_stream(message)
        except Exception as e:
            print(f"获取ai结果异常: {e}")
            content = str(e)
        end_time = time.time()
        # 耗时取整数
        time_cost = int(end_time - start_time)
        print()
        print(f"耗时:{time_cost}s")
        print()
        # print(f"耗时:{time_cost}s \nAI 回复：{content}")
        insert_message_info(dbpath, id, message, content, time_cost)


if __name__ == "__main__":
    main()
