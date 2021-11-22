from proxyPool.conf import REDIS_MAX_THRESHOLD
from proxyPool.redisOperation import RedisOperator
from schedule.PoolTester import UsabilityTester
from proxyPool.Spider import SpiderGen
from concurrent import futures
from proxyPool.ReWriteError import SourceDepletionError


class PoolAdder(object):
    def __init__(self):
        self.threshold = REDIS_MAX_THRESHOLD
        self.redis_operator = RedisOperator()
        self.proxy_tester = UsabilityTester()

    def is_full(self):
        return True if self.redis_operator.size >= self.threshold else False

    def add_to_pool(self):
        spiders = [cls() for cls in SpiderGen.spiders]
        flag = 0

        while not self.is_full():
            flag += 1
            raw_proxies = []
            with futures.ThreadPoolExecutor(max_workers=len(spiders)) as executor:
                future_to_down = {executor.submit(spiders[i].gets, 10): i for i in range(len(spiders))}
                for future in futures.as_completed(future_to_down):
                    raw_proxies.extend(future.result())

            print(raw_proxies)
            self.proxy_tester.set_arg(raw_proxies)
            self.proxy_tester.tester()
            proxies = self.proxy_tester.usable_proxies

            if len(proxies) != 0:
                self.redis_operator.puts(proxies)
            if self.is_full():
                break
            if flag >= 20:
                raise SourceDepletionError
