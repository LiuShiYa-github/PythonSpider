# Scrapy settings for Che168 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Che168'

SPIDER_MODULES = ['Che168.spiders']
NEWSPIDER_MODULE = 'Che168.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Che168 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 注释情况:禁用cookie
# 取消注释,并设置为False: 找settings.py中DEFAULT_REQUEST_HEADERS中的Cookie
# 取消注释,并设置为True: 找爬虫文件中Request()方法中的cookies参数,或者中间件
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  # 'Cookie': 'listuserarea=0; fvlid=1648533656121wZzAly78Pujb; sessionid=fc7acfdf-a782-43d6-a683-7f3bc3a0184d; che_sessionid=C928320C-5B67-4645-9B2A-4047E35432CD%7C%7C2022-03-29+14%3A00%3A57.962%7C%7Cwww.autohome.com.cn; v_no=9; visit_info_ad=C928320C-5B67-4645-9B2A-4047E35432CD||66A85397-DE0C-4D69-A9FE-6A61BB7D7EC8||-1||-1||9; userarea=0; Hm_lvt_d381ec2f88158113b9b76f14c497ed48=1648533657,1648564344; sessionip=58.100.81.5; area=330106; sessionvisit=fb2210dd-ce95-4157-9dd5-3c236792c9a4; sessionvisitInfo=fc7acfdf-a782-43d6-a683-7f3bc3a0184d||102179; che_ref=www.autohome.com.cn%7C0%7C110965%7C0%7C2022-03-29+22%3A32%3A24.192%7C2022-03-29+14%3A00%3A57.962; che_sessionvid=1216C332-21F9-44BC-A2B3-4B91FB2C0093; sessionuid=fc7acfdf-a782-43d6-a683-7f3bc3a0184d; ahpvno=24; Hm_lpvt_d381ec2f88158113b9b76f14c497ed48=1648564358; ahuuid=B3E2A8DB-C0E3-42FE-9D5D-3296642725F7; showNum=24',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
}
LOG_LEVEL = 'WARNING'
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Che168.middlewares.Che168SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'Che168.middlewares.Che168DownloaderMiddleware': 543,
   'Che168.middlewares.Che168RandomUserAgentDownloaderMiddleware': 200,
   # 'Che168.middlewares.Che168RandomProxyDownloaderMiddleware': 100,
   'Che168.middlewares.Che168RandomCookieDownloaderMiddleware': 300,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Che168.pipelines.Che168Pipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
