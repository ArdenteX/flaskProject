import asyncio
import aiohttp

test_api = 'https://www.baidu.com'


class UsabilityTester(object):
    def __init__(self):
        self.raw_proxies = None
        self.usable_proxies = None

    def set_arg(self, raw_proxies):
        self.raw_proxies = raw_proxies
        self.usable_proxies = []

    async def _test_single_proxy(self, proxy):
        async with aiohttp.ClientSession() as session:
            real_proxy = 'http://' + proxy
            try:
                async with session.get(url=test_api, proxy=real_proxy, timeout=15) as resp:
                    self.usable_proxies.append(real_proxy)
            except Exception:
                print(Exception.__name__)

    def tester(self):
        print("Tester is working")
        tasks = [self._test_single_proxy(proxy) for proxy in self.raw_proxies]
        asyncio.run(asyncio.wait(tasks))

    @property
    def _get_usable_proxies(self):
        return self.usable_proxies
