# 设置变量
import requests
import logging
import json
# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s-%(name)s][%(lineno)d][%(funcName)s][%(levelname)s]%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    encoding='utf-8')
logger = logging.getLogger(__name__)

# 环境变量配置
env_map = {
    "dev": {
        "url": "https://echo.apifox.com/"
    },
    "prod": {
        "url": "https://api.example.com"
    },
    "test": {
        "url": "http://localhost:8000"
    }
}

# 多环境切换


def get_url(env: str) -> str:
    """
    Returns the URL of the API
    """
    if env in env_map:
        return env_map[env]["url"]
    return ""


def get_token():
    """
    获取 token 的逻辑 需要根据项目的情况自行实现
    """
    return ""


def get(url):
    """
    发送一个带有Bearer Token的GET请求到指定的URL，并返回JSON响应数据。

    参数:
    - url (str): 目标API的URL。
    - token (str): 用于认证的Bearer Token。

    返回:
    - dict: API响应的JSON数据。

    异常:
    - requests.exceptions.RequestException: 网络请求过程中发生的错误。
    """
    headers = {
        'Authorization': f'Bearer {token}',
    }
    try:
        logger.info(f"发送 get 请求 ===> url:[{url}],token:[{token}]")
        response = requests.get(url, headers=headers)
        # 转成 json 字符串并格式化打印
        data = response.json()
        logging.info(
            f"请求结果: ===> \n{json.dumps(data, indent=4,ensure_ascii=False)}")
        # 如果响应状态不是200，将抛出HTTPError异常
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.info(f"response.text = {response.text}")
        logging.error(f"请求发生错误: {e}")
        return None


def post_json(url, payload):
    """
    向指定URL发送POST请求，并返回JSON响应数据。

    参数:
    - url (str): 目标API的URL。
    - payload (dict): 要发送的数据，格式为字典。

    返回:
    - dict: API响应的JSON数据。

    异常:
    - requests.exceptions.RequestException: 网络请求过程中发生的错误。
    """
    try:
        # 使用json参数自动设置Content-Type为application/json
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }
        logger.info(f"请求 url:{url},token:{token}")
        logger.info(f"请求 json:")
        logging.info(payload)
        response = requests.post(url, data=payload, headers=headers)
        # 转成 json 字符串并格式化打印
        data = response.json()
        logging.info(
            f"请求结果: ===> \n{json.dumps(data, indent=4,ensure_ascii=False)}")
        logging.info(f"请求结果: ===> \n{json.dumps(data, indent=4)}")
        # 如果响应状态不是200，将抛出HTTPError异常
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.info(f"response.text = {response.text}")
        logger.info(f"请求发生错误: {e}")
        return None
