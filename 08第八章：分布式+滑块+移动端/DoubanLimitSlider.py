#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: DoubanLimitSlider.py
@Time    : 2022/4/9 12:49
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 登录豆瓣网的极限滑块验证
"""
from selenium import webdriver
# 导入鼠标类
from selenium.webdriver import ActionChains
import time

# 加速度函数
def get_tracks(distance):
    v = 0
    t = 0.3
    tracks = []
    current = 0
    mid = distance*4/5
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        s = v0*t+0.5*a*(t**2)
        current += s
        tracks.append(round(s))
        v = v0 + a*t
    return tracks

# 1、打开豆瓣官网 - 并将窗口最大化
driver = webdriver.Chrome()
driver.get('https://www.douban.com/')
# 2、切换到iframe子页面
iframe_node = driver.find_element_by_xpath('//div[@class="login"]/iframe')
driver.switch_to.frame(iframe_node)
# 3、密码登录 + 用户名 + 密码 + 登录豆瓣
driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys('17695691664')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('liushiya111')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
time.sleep(5)
# 4、切换到新的iframe子页面 - 滑块验证
verify_iframe = driver.find_element_by_xpath('//*[@id="tcaptcha_iframe"]')
driver.switch_to.frame(verify_iframe)
# 5、按住开始滑动位置按钮 - 先移动180个像素
start_node = driver.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
ActionChains(driver).click_and_hold(on_element=start_node).perform()
# 移动到举例某个节点多少距离的位置
ActionChains(driver).move_to_element_with_offset(to_element=start_node, xoffset=180, yoffset=0).perform()
# 6、使用加速度函数移动剩下的举例
tracks = get_tracks(22)
for track in tracks:
    # move_bu_offset:鼠标从当前位置移动多少的举例
    ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()
# 7、延迟释放鼠标: release()
time.sleep(1)
ActionChains(driver).release().perform()
