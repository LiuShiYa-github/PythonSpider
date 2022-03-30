# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
import random
from .proxies import proxy_list
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class Che168SpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Che168DownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# 中间件 - 随机User-Agent
class Che168RandomUserAgentDownloaderMiddleware(object):
    def process_request(self, request, spider):
        agent = UserAgent().random
        request.headers['User-Agent'] = agent
        print(agent)
        
        
# 中间件 - 代理IP地址
class Che168RandomProxyDownloaderMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(proxy_list)
        # 如何包装到请求对象? 使用某个属性,meta属性
        # meta:在不同解析函数之间传递数据,又可以定以代理
        request.meta['proxy'] = proxy
        print(proxy)

    def process_exception(self, request, exception, spider):
        """ 处理异常的函数,因为代理IP可能不能使用 scrapy会自动尝试3次,我们想让它一直尝试 """
        return request


# 中间件 - 代理IP地址
class Che168RandomCookieDownloaderMiddleware(object):
    def process_request(self, request, spider):
        cookie_dict = self.get_cookies()
        # 用什么属性添加cookie中间件? 答案是 cookies属性
        request.cookies = cookie_dict
        print(cookie_dict)
        
    def get_cookies(self):
        cookie_string = 'listuserarea=0; fvlid=1648533656121wZzAly78Pujb; sessionid=fc7acfdf-a782-43d6-a683-7f3bc3a0184d; che_sessionid=C928320C-5B67-4645-9B2A-4047E35432CD%7C%7C2022-03-29+14%3A00%3A57.962%7C%7Cwww.autohome.com.cn; v_no=9; visit_info_ad=C928320C-5B67-4645-9B2A-4047E35432CD||66A85397-DE0C-4D69-A9FE-6A61BB7D7EC8||-1||-1||9; userarea=0; Hm_lvt_d381ec2f88158113b9b76f14c497ed48=1648533657,1648564344; sessionip=58.100.81.5; area=330106; sessionvisit=fb2210dd-ce95-4157-9dd5-3c236792c9a4; sessionvisitInfo=fc7acfdf-a782-43d6-a683-7f3bc3a0184d||102179; che_ref=www.autohome.com.cn%7C0%7C110965%7C0%7C2022-03-29+22%3A32%3A24.192%7C2022-03-29+14%3A00%3A57.962; che_sessionvid=1216C332-21F9-44BC-A2B3-4B91FB2C0093; sessionuid=fc7acfdf-a782-43d6-a683-7f3bc3a0184d; ahpvno=24; Hm_lpvt_d381ec2f88158113b9b76f14c497ed48=1648564358; ahuuid=B3E2A8DB-C0E3-42FE-9D5D-3296642725F7; showNum=24'
        cokie_dict = {}
        for kv in cookie_string.split('; '):
            k = kv.split('=')[0]
            v = kv.split('=')[1]
            cokie_dict[k] = v
        return cokie_dict