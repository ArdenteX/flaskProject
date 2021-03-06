import asyncio
import aiohttp

test_api = 'http://httpbin.org/ip'


class UsabilityTester(object):
    def __init__(self):
        self.raw_proxies = None
        self._usable_proxies = None

    def set_arg(self, raw_proxies):
        self.raw_proxies = raw_proxies
        self._usable_proxies = []

    async def _test_single_proxy(self, proxy):
        async with aiohttp.ClientSession() as session:
            real_proxy = 'http://' + proxy
            real_ip = 'http://' + str(proxy).split(":")[0]
            try:
                async with session.get(url=test_api, proxy=real_proxy, timeout=15) as resp:
                    json = await resp.json()
                    print("response's ip:", str(json['origin']))
                    print("real proxy ip: ", real_proxy)
                    print("type of json, ", type(json['origin']))
                    splicing_origin = 'http://' + str(json['origin'])
                    print("ip after splice: ", splicing_origin)
                    if splicing_origin == real_ip:
                        print("This ip is high hide proxy!")
                        self._usable_proxies.append(real_proxy)

            except Exception:
                print(real_proxy, 'unusable... ', Exception.__name__, " ... ")

    def tester(self):
        print("Tester is working")
        tasks = [self._test_single_proxy(proxy) for proxy in self.raw_proxies]
        print("proxy's number = ", len(tasks))
        asyncio.run(asyncio.wait(tasks))

    @property
    def get_usable_proxies(self):
        return self._usable_proxies
