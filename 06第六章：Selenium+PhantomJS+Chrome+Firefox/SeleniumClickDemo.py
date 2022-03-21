#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: SeleniumClickDemo.py
@Time    : 2022/3/21 21:22
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 打开百度并点击搜索
"""
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 1.找到搜索的节点框,并发送搜索关键字,selenium 是以前端渲染的内容为主,不再是以实际响应内容为主了.
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('吴尊')
driver.find_element_by_xpath('//*[@id="su"]').click()
# 2.浏览器窗口最大化
driver.maximize_window()
# time.sleep(3)
# 3.获取屏幕截图
driver.save_screenshot('baidu.png')
# 4.关闭浏览器
# driver.quit()
# 5.打印前端HTML源码(前端源码而不是响应内容)
# html = driver.page_source
# print(html)
# 6.find():在HTML结构源码中查找某个字符串是否存在,记住:查找失败,返回-1.用于判断是否为最后一页
print(driver.page_source.find('aaa'))
driver.quit()


