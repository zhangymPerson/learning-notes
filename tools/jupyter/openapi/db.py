import pymysql


class DB():
    """
    类的作用是:
        获取 mysql 连接
    Attributes:
        params: type
    """

    def __init__(self, host='localhost', port=3306, db_name='', user='root', passwd='root', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(
            host=host, port=port, db=db_name, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

# 根据环境名获取数据库中的配置信息


def get_base_config(env: str) -> dict:
    db_name = "openapi"
    with DB(host='127.0.0.1', user='root', passwd='12345678', db_name=db_name) as db:
        db.execute(
            f"select * from {db_name}.openapi_env where env_name='{env}'")
        config = db.fetchone()
        return config


def get_base_url(env: str) -> str:
    config = get_base_config(env)
    return config.get("base_url")


def get_variable(env: str) -> dict:
    config = get_base_config(env)
    return config.get("variables")


def get_openapi_id(id: int) -> dict:
    db_name = "openapi"
    with DB(host='127.0.0.1', user='root', passwd='12345678', db_name=db_name) as db:
        db.execute(
            f"select * from {db_name}.openapi where id={id}")
        config = db.fetchone()
        return config


def test():
    config = get_openapi_id(1)
    print(config)

# test()
