import requests

print("Hello, World!")

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


def get_url(env: str) -> str:
    """
    Returns the URL of the API
    """
    if env in env_map:
        return env_map[env]["url"]
    return ""


def get_token(env: str) -> str:
    """
    Returns the token of the API
    """
    url = get_url(env)
    url = url + "/post"
    body = {
        "username": "admin",
        "password": "admin",
        "token": f"token is {env} token"
    }
    req = requests.post(url, json=body)
    # token 在 data 中的 access_token 字段中
    token = req.json().get("json", {}).get("token", "")
    return token
