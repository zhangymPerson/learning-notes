import argparse
import http.client
import json


def get_admin_token():
    conn = http.client.HTTPConnection("127.0.0.1", 8080)
    payload = json.dumps({
        "username": "admin",
        "password": "admin",
        "refresh": True,
        "provider": "db"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
    conn.request("POST", "/api/v1/security/login", payload, headers)
    res = conn.getresponse()
    data = res.read()
    # 转换为字典
    data = json.loads(data)
    return data.get('access_token')


def get_embed_token(id: str):
    conn = http.client.HTTPConnection("127.0.0.1", 8080)
    payload = json.dumps({
        "user": {
            "username": "admin",
            "first_name": "",
            "last_name": ""
        },
        "resources": [
            {
                "type": "dashboard",
                "id": id
            }
        ],
        "rls": []
    })
    token = get_admin_token()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {token}",
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
    conn.request("POST", "/api/v1/security/guest_token/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    if res.status != 200:
        print(res.status, res.reason)
        print(data.decode("utf-8"))
        return None
    data = json.loads(data)
    return data.get('token')


def main():
    """
    主要是处理
    """
    # 脚本参数 -i --id 输入id
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--id", help="id 必须传入,id 为 Embed 的 id", required=False)
    args = parser.parse_args()
    id = args.id
    if id is None or id == "":
        parser.print_help()
        return
    token = get_embed_token(id)
    print(f"id = {id}\ntoken =\n{token}")


if __name__ == "__main__":
    main()
