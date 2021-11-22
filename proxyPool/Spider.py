from proxyPool.tools import get_page
from proxyPool.ReWriteError import ReWriteSpiderError
import time


class SpiderGen(type):
    spiders = []

    def _init(cls):
        cls.count = 1

    def _plus(cls, count):
        cls.count += count

    def _flush(cls):
        cls.count = 1

    def __new__(cls, *args, **kwargs):
        if 'gets' not in args[2]:
            raise ReWriteSpiderError(args[0])

        args[2]['__init__'] = lambda self: SpiderGen._init(self)
        args[2]['_plus'] = lambda self, count: SpiderGen._plus(self, count)
        args[2]['_flush'] = lambda self: SpiderGen._flush(self)
        SpiderGen.spiders.append(type.__new__(cls, *args, **kwargs))
        return type.__new__(cls, *args, **kwargs)


class Daili666Spider(metaclass=SpiderGen):
    start_url = 'http://www.66ip.cn/{}.html'

    def gets(self, page_total=3):
        print("daili666 crawl is working")
        urls = [self.start_url.format(i)
                for i in range(self.count, self.count + page_total)]
        self._plus(page_total)
        ans = []
        for url in urls:
            soup = get_page(url)
            # 防止被 Ban, 加 1s 的间隔。
            time.sleep(1)
            proxy_list = soup.find('table', {"border": "2px"})
            for proxy in proxy_list.find_all('tr')[1:]:
                ip = proxy.find_all('td')[0].get_text()
                port = proxy.find_all('td')[1].get_text()
                ans.append(':'.join([ip, port]))
        return ans


class XiLaProxySpider(metaclass=SpiderGen):
    start_url = 'http://www.xiladaili.com/gaoni/{}/'

    def gets(self, page_total=3):
        print("xila crawl is working")
        urls = [self.start_url.format(i) for i in range(self.count, self.count + page_total)]
        self._plus(page_total)
        ans = []
        for url in urls:
            try:
                time.sleep(1)
                soup = get_page(url)
                proxy_list = soup.find('table', {"class": 'fl-table'}).find('tbody')

                for proxy in proxy_list.find_all('tr'):
                    tmp = proxy.find_all('td')
                    ip_port = tmp[0].get_text().split(':')
                    ans.append(':'.join([ip_port[0], ip_port[1]]))
            except Exception:
                print(Exception.__name__)

        return ans


class KuaidailiSpider(metaclass=SpiderGen):
    start_url = 'http://www.kuaidaili.com/free/inha/{}/'

    def gets(self, page_total=2):
        print('kuaidaili crawl is working')
        urls = [self.start_url.format(i)
                for i in range(self.count, self.count + page_total)]
        self._plus(page_total)
        ans = []
        for url in urls:
            soup = get_page(url)
            time.sleep(1)
            proxy_list = soup.find('table',
                                   {'class': 'table table-bordered table-striped'}) \
                .find('tbody')
            for proxy in proxy_list.find_all('tr'):
                tmp = proxy.find_all('td')
                ip = tmp[0].get_text()
                port = tmp[1].get_text()
                ans.append(':'.join([ip, port]))
        return ans





