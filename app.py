from flask import Flask, g
from proxyPool.redisOperation import RedisOperator

app = Flask(__name__)


def get_conn():
    """获取 Redis 连接
    :return: RedisOperator
    """
    if not hasattr(g, 'redis_connect'):
        g.redis_connect = RedisOperator()
    return g.redis_connect


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/get')
def get_proxy():
    conn = get_conn()
    return conn.pop()


@app.route('/count')
def get_counts():
    """Get the count of proxies
    :return: HTML
    """
    pool = get_conn()
    return str(pool.size)


if __name__ == '__main__':
    app.run()
