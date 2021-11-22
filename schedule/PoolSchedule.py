import time
from multiprocessing import Process
from proxyPool.redisOperation import RedisOperator
from proxyPool.conf import REDIS_MAX_THRESHOLD
from proxyPool.conf import REDIS_LOW_THRESHOLD
from schedule.PoolTester import UsabilityTester
from schedule.PoolAdder import PoolAdder


class ExpireCheckProcess(Process):
    def __init__(self, cycle):
        Process.__init__(self)
        self.cycle = cycle
        self._tester = UsabilityTester()

    def run(self):
        print("Expire Check Process Is Working...")
        redis_pool = RedisOperator()
        while True:
            time.sleep(self.cycle)
            total = int(0.25*len(redis_pool.size))
            if total < 4:
                continue

            raw_proxies = [redis_pool.pop() for _ in range(total)]
            self._tester.set_arg(raw_proxies)
            self._tester.tester()
            usable_proxies = self._tester.get_usable_proxies
            if len(usable_proxies) != 0:
                redis_pool.puts(usable_proxies)


class ProxiesCountProcess(Process):
    def __init__(self, cycle):
        Process.__init__(self)
        self._max_threshold = REDIS_MAX_THRESHOLD
        self._low_threshold = REDIS_LOW_THRESHOLD
        self._cycle = cycle

    def run(self):
        print("Proxies Count Process Is Working....")
        pool_adder = PoolAdder()
        redis_pool = RedisOperator()
        print("Pool Size: ", redis_pool.size)
        while True:
            if redis_pool.size < self._low_threshold:
                pool_adder.add_to_pool()
            time.sleep(self._cycle)

