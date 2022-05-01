# PythonSpider

[![Python Version](https://img.shields.io/badge/python-3.8+-green)](https://www.python.org)
<a href="https://github.com/LiuShiYa-github/PythonSpider/blob/master/Image/wx.jpg" target="_blank"><img src="https://img.shields.io/badge/weChat-微信-blue.svg" alt="微信"></a>
<a href="https://blog.csdn.net/weixin_42506599?spm=1000.2115.3001.5343" target="_blank"><img src="https://img.shields.io/badge/csdn-CSDN-red.svg" alt="CSDN"></a>
[![CI status](https://github.com/smicallef/spiderfoot/workflows/Tests/badge.svg)](https://github.com/LiuShiYa-github/PythonSpider/actions)
![img.png](Image/readme.png)

## 声明
* 此repo是纪录学习Python爬虫阶段的代码与笔记，学习视频来源于网络
* 代码、教程**仅限于学习交流，请勿用于任何商业用途！**

## 知识点
<details>
<summary>👉查看涉及的知识点</summary>

**第一章**
```text
01 网络爬虫概述
02 urllib.request原理以及使用
03 正则表达式re使用
```

**第二章**
```text
01 数据持久化存储-csv
02 数据持久化存储-MySQL
03 数据持久化存储-MongoDB
04 requests模块
05 增量爬虫-基于MySQL及Redis实现
```

**第三章**
```text
01 爬虫-图片抓取
02 xpath语法解析
03 lxml+xpath解析提取数据
```

**第四章**
```text
01 requests模块高级使用
02 代理ip使用
03 POST请求数据抓取
```

**第五章**
```text
01 动态加载数据爬取
02 JSON解析模块及全站抓取
03 多线程爬虫
04 多级页面多线程爬取
05 Cookie模拟登录
```


**第六章**
```text
01 Selenium+PhantomJS Chrome Firefox
02 Selenium常用方法
03 Selenium高级操作
```

**第七章**
```text
01 Scrapy框架原理
02 Scrapy配置文件解析
03 中间件
04 Scrapy处理POST请求
05 Scrapy之图片管道
06 Scrapy之文件管道
```

**第八章**
```text
01 Scrapy之分布式爬虫原理
02 Scrapy之分布式爬虫实现
03 机器视觉与tesseract
04 移动端数据抓取
```
</details>

## 实例

<details>
<summary>👉查看实例</summary>

* [抓取贴吧HTML](https://github.com/LiuShiYa-github/PythonSpider/blob/master/01%E7%AC%AC%E4%B8%80%E7%AB%A0%EF%BC%9A%E7%88%AC%E8%99%AB%E6%A6%82%E8%BF%B0%2Burllib%2Bre/TiebaSpider.py "悬停显示")
* [猫眼经典电影-保存为CSV-单行保存](https://github.com/LiuShiYa-github/PythonSpider/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%95%B0%E6%8D%AE%E6%8C%81%E4%B9%85%E5%8C%96%2Brequests/MaoyanClassicMovieCSVWriterow.py "悬停显示")
* [猫眼经典电影-保存为CSV-多行保存](https://github.com/LiuShiYa-github/PythonSpider/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%95%B0%E6%8D%AE%E6%8C%81%E4%B9%85%E5%8C%96%2Brequests/MaoyanClassicMovieCSVWriterows.py "悬停显示")
* [猫眼电影经典影片-存储到MySQL](https://github.com/LiuShiYa-github/PythonSpider/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%95%B0%E6%8D%AE%E6%8C%81%E4%B9%85%E5%8C%96%2Brequests/MaoyanClassicMovieMysql.py "悬停显示")
* [猫眼电影经典影片-存储到MongoDB](https://github.com/LiuShiYa-github/PythonSpider/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%95%B0%E6%8D%AE%E6%8C%81%E4%B9%85%E5%8C%96%2Brequests/MaoyanClassicMovieMongoDB.py "悬停显示")
* [汽车之家基于Redis实现增量爬虫](https://github.com/LiuShiYa-github/PythonSpider/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%95%B0%E6%8D%AE%E6%8C%81%E4%B9%85%E5%8C%96%2Brequests/CarHomeSpiderIncrementalRedis.py "悬停显示")
* [汽车之家Mysql实现增量爬虫](https://github.com/LiuShiYa-github/PythonSpider/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%95%B0%E6%8D%AE%E6%8C%81%E4%B9%85%E5%8C%96%2Brequests/CarHomeSpiderMysqlIncre.py "悬停显示")
* [图片抓取-爬取wallhaven.cc](https://github.com/LiuShiYa-github/PythonSpider/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alxml%2Bxpath/SpiderWallhavenSelenimu.py "悬停显示")
* [基于xpath抓取链家二手房源](https://github.com/LiuShiYa-github/PythonSpider/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alxml%2Bxpath/LianHomeSpider.py "悬停显示")
* [requests.post请求有道翻译结果抓取](https://github.com/LiuShiYa-github/PythonSpider/blob/master/04%E7%AC%AC%E5%9B%9B%E7%AB%A0%EF%BC%9Arequests%E7%9A%84%E9%AB%98%E7%BA%A7%E4%BD%BF%E7%94%A8/PostYoudaoTranslate.py "悬停显示")
* [requests.proxies抓取飞度代理的免费高匿代理并测试可用性](https://github.com/LiuShiYa-github/PythonSpider/blob/master/04%E7%AC%AC%E5%9B%9B%E7%AB%A0%EF%BC%9Arequests%E7%9A%84%E9%AB%98%E7%BA%A7%E4%BD%BF%E7%94%A8/ProxyIpPool.py "悬停显示")
* [汽车之家数据抓取-两级页面](https://github.com/LiuShiYa-github/PythonSpider/blob/master/05%E7%AC%AC%E4%BA%94%E7%AB%A0%EF%BC%9A%E5%A4%9A%E7%BA%A7%E9%A1%B5%E9%9D%A2%2B%E5%A4%9A%E7%BA%BF%E7%A8%8B%2BCookie%E7%99%BB%E5%BD%95/CarHomeSpider.py "悬停显示")
* [豆瓣剧情电影排行榜](https://github.com/LiuShiYa-github/PythonSpider/blob/master/05%E7%AC%AC%E4%BA%94%E7%AB%A0%EF%BC%9A%E5%A4%9A%E7%BA%A7%E9%A1%B5%E9%9D%A2%2B%E5%A4%9A%E7%BA%BF%E7%A8%8B%2BCookie%E7%99%BB%E5%BD%95/DoubanPlotSpider.py "悬停显示")
* [豆瓣全站的电影](https://github.com/LiuShiYa-github/PythonSpider/blob/master/05%E7%AC%AC%E4%BA%94%E7%AB%A0%EF%BC%9A%E5%A4%9A%E7%BA%A7%E9%A1%B5%E9%9D%A2%2B%E5%A4%9A%E7%BA%BF%E7%A8%8B%2BCookie%E7%99%BB%E5%BD%95/DoubanPlotStorageJsonSpider.py "悬停显示")
* [华为应用市场社交类app](https://github.com/LiuShiYa-github/PythonSpider/blob/master/05%E7%AC%AC%E4%BA%94%E7%AB%A0%EF%BC%9A%E5%A4%9A%E7%BA%A7%E9%A1%B5%E9%9D%A2%2B%E5%A4%9A%E7%BA%BF%E7%A8%8B%2BCookie%E7%99%BB%E5%BD%95/HuaweiAppMultithreading.py "悬停显示")
* [多线程抓取腾讯招聘](https://github.com/LiuShiYa-github/PythonSpider/blob/master/05%E7%AC%AC%E4%BA%94%E7%AB%A0%EF%BC%9A%E5%A4%9A%E7%BA%A7%E9%A1%B5%E9%9D%A2%2B%E5%A4%9A%E7%BA%BF%E7%A8%8B%2BCookie%E7%99%BB%E5%BD%95/MultilevelPageMultithreading.py "悬停显示")
* [selenium无头浏览器方式获取京东商城爬虫类的图书](https://github.com/LiuShiYa-github/PythonSpider/blob/master/06%E7%AC%AC%E5%85%AD%E7%AB%A0%EF%BC%9ASelenium%2BPhantomJS%2BChrome%2BFirefox/JdSeleniumOptionsSpider.py "悬停显示")
* [使用selenium模拟登录QQ邮箱](https://github.com/LiuShiYa-github/PythonSpider/blob/master/06%E7%AC%AC%E5%85%AD%E7%AB%A0%EF%BC%9ASelenium%2BPhantomJS%2BChrome%2BFirefox/SeleniumLoginQQmail.py "悬停显示")
* [抓取网易云音乐排行榜](https://github.com/LiuShiYa-github/PythonSpider/blob/master/06%E7%AC%AC%E5%85%AD%E7%AB%A0%EF%BC%9ASelenium%2BPhantomJS%2BChrome%2BFirefox/SeleniumWangyiyunMusic.py "悬停显示")
* [使用selenium抓取最新行政区化代码](https://github.com/LiuShiYa-github/PythonSpider/blob/master/06%E7%AC%AC%E5%85%AD%E7%AB%A0%EF%BC%9ASelenium%2BPhantomJS%2BChrome%2BFirefox/SeleniumLoginQQmail.py "悬停显示")
* [Scrapy抓取二手车之家](https://github.com/LiuShiYa-github/PythonSpider/tree/master/07%E7%AC%AC%E4%B8%83%E7%AB%A0%EF%BC%9AScrapy%E6%A1%86%E6%9E%B6%2B%E4%B8%AD%E9%97%B4%E4%BB%B6/Che168-middlewares "悬停显示")
* [盗墓笔记全系列](https://github.com/LiuShiYa-github/PythonSpider/tree/master/07%E7%AC%AC%E4%B8%83%E7%AB%A0%EF%BC%9AScrapy%E6%A1%86%E6%9E%B6%2B%E4%B8%AD%E9%97%B4%E4%BB%B6/Daomu "悬停显示")
* [瓜子二手车](https://github.com/LiuShiYa-github/PythonSpider/tree/master/07%E7%AC%AC%E4%B8%83%E7%AB%A0%EF%BC%9AScrapy%E6%A1%86%E6%9E%B6%2B%E4%B8%AD%E9%97%B4%E4%BB%B6/Guazi "悬停显示")
* [肯德基门店](https://github.com/LiuShiYa-github/PythonSpider/tree/master/07%E7%AC%AC%E4%B8%83%E7%AB%A0%EF%BC%9AScrapy%E6%A1%86%E6%9E%B6%2B%E4%B8%AD%E9%97%B4%E4%BB%B6/KFC "悬停显示")
* [Scrapy三层以上页面抓取PPT模板](https://github.com/LiuShiYa-github/PythonSpider/tree/master/07%E7%AC%AC%E4%B8%83%E7%AB%A0%EF%BC%9AScrapy%E6%A1%86%E6%9E%B6%2B%E4%B8%AD%E9%97%B4%E4%BB%B6/PPT "悬停显示")
* [360浏览器美眉图片抓取](https://github.com/LiuShiYa-github/PythonSpider/tree/master/07%E7%AC%AC%E4%B8%83%E7%AB%A0%EF%BC%9AScrapy%E6%A1%86%E6%9E%B6%2B%E4%B8%AD%E9%97%B4%E4%BB%B6/SO "悬停显示")
* [豆瓣滑块验证码](https://github.com/LiuShiYa-github/PythonSpider/blob/master/08%E7%AC%AC%E5%85%AB%E7%AB%A0%EF%BC%9A%E5%88%86%E5%B8%83%E5%BC%8F%2B%E6%BB%91%E5%9D%97%2B%E7%A7%BB%E5%8A%A8%E7%AB%AF/DoubanLimitSlider.py "悬停显示")
* [pytesseract识别图片](https://github.com/LiuShiYa-github/PythonSpider/blob/master/08%E7%AC%AC%E5%85%AB%E7%AB%A0%EF%BC%9A%E5%88%86%E5%B8%83%E5%BC%8F%2B%E6%BB%91%E5%9D%97%2B%E7%A7%BB%E5%8A%A8%E7%AB%AF/Pytesseract.py "悬停显示")

</details>