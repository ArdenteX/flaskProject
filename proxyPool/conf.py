import my_fake_useragent
# redis host
REDIS_HOST = 'localhost'

# redis port
REDIS_PORT = 6379

# redis name
REDIS_NAME = 'proxies'

REDIS_MAX_THRESHOLD = 60
REDIS_LOW_THRESHOLD = 20

VALID_CHECK_CYCLE = 600
POOL_LEN_CHECK_CYCLE = 20

HEADERS = {
    'User-agent': my_fake_useragent.UserAgent().random(),
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}
