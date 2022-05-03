# Scrapy之分布式爬虫原理

**原理和实现**
```text
定义：
    分布式爬虫即多台爬虫服务器同时爬取一个爬虫项目，数据不重复
分布式爬虫原理：
    多台主机共享一个爬取队列
分布式爬虫实现：
    重写scrapy的调度器 - 即 scrapy_redis模块
scrapy_redis安装：
    sudo pip install  scrapy_redis

scrapy_redis分布式实现流程：
    ①scrapy_redis就是建立一个Redis队列
    ②调度器把爬虫文件生成的请求发送给Redis队列
    ③再用调度器从Redis队列中取出请求
    ④其他爬虫也可以从队列中取出请求
    ⑤每一个爬虫的调度器都从队列中取出请求和存入请求，这样实现多个爬虫，多台机器同时爬取的目标
    
Redis的优势：
    Redis基于内存，速度快，可快速存取请求
    Redis中集合数据类型无序去重的特点，用来存储每个请求的指纹
```

**scrapy_redis详解**

```text
settings.py配置说明：
    # 指定使用scrapy_redis调度器
    SCHEDULER = "scrapy_redis.scheduler.Scheduler"
    # 指定使用scrapy_redis去重机制
    DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
    # 指定redis的IP地址和端口号
    REDIS_URL = 'redis://root:123456@10.0.0.101:6379'
    # 添加scrapy_redis管道 把数据真正存在redis数据库
    # 爬取后不清理请求指纹
    SCHEDULER_PERSIST = True
```

# Scrapy之分布式爬虫实现

**分布式实现流程**
```text
完整正常Scrapy爬虫项目：
    因为Scrapy本身不支持分布式，所以需要先写非分布式爬虫

利用scrapy_redis实现分布式爬虫：
    方法一： 配置settings.py实现
    方法二： 使用redis_key实现
```

[Scrapy分布式爬虫-腾讯招聘](https://github.com/LiuShiYa-github/PythonSpider/tree/master/08%E7%AC%AC%E5%85%AB%E7%AB%A0%EF%BC%9A%E5%88%86%E5%B8%83%E5%BC%8F%2B%E6%BB%91%E5%9D%97%2B%E7%A7%BB%E5%8A%A8%E7%AB%AF/Tencent)

![img_74.png](../Image/img_74.png)

# 机器视觉与tesseract

**重要概念**

```text
OCR:
    光学字符识别，通过扫描等光学输入方式将各种票据、报刊、书籍、文稿及其他印刷品的文字转换为图像信息，再利用文字识别技术将图像信息转换为电子文本
tesseract-ocr：
    OCR的一个底层识别库，由google维护的开源OCR识别库
pytesseract：
    Python模块，是对tesseract-ocr做的一层API封装
```

[pytesseract识别图片](https://github.com/LiuShiYa-github/PythonSpider/blob/master/08%E7%AC%AC%E5%85%AB%E7%AB%A0%EF%BC%9A%E5%88%86%E5%B8%83%E5%BC%8F%2B%E6%BB%91%E5%9D%97%2B%E7%A7%BB%E5%8A%A8%E7%AB%AF/Pytesseract.py "悬停显示")

![img_75.png](../Image/img_75.png)



#移动端数据抓取

[移动端数据抓取-有道翻译](https://github.com/LiuShiYa-github/PythonSpider/blob/master/08%E7%AC%AC%E5%85%AB%E7%AB%A0%EF%BC%9A%E5%88%86%E5%B8%83%E5%BC%8F%2B%E6%BB%91%E5%9D%97%2B%E7%A7%BB%E5%8A%A8%E7%AB%AF/Mobilephone_youdao.py "悬停显示")

![img_73.png](../Image/img_73.png)