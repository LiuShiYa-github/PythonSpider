#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: outlook.py
@Time    : 2022/4/11 20:49
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 通过Outlook获取公司员工的部门信息
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xlrd


class GetDepartment:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(
            url='https://login.partner.microsoftonline.cn/common/oauth2/authorize?client_id=00000002-0000-0ff1-ce00-000000000000&redirect_uri=https%3a%2f%2fpartner.outlook.cn%2fowa%2f&resource=00000002-0000-0ff1-ce00-000000000000&response_mode=form_post&response_type=code+id_token&scope=openid&msafed=0&msaredir=0&client-request-id=9fa590fb-0d9f-f007-3a8a-61fbfc83bd0d&protectedtoken=true&claims=%7b%22id_token%22%3a%7b%22xms_cc%22%3a%7b%22values%22%3a%5b%22CP1%22%5d%7d%7d%7d&nonce=637852785208449284.53722b9c-b1ce-4f4b-a327-5c64b749f25d&state=Fcu7DoIwFIDhVt_FrdIeTikdiCPE4GIMkbE3EhIJCSCXt7cO37_9lBByjk4R5TFEZanKJfzxHFFDjleZKgCrHbPCBYYdWmZSUEy6DK1C3YH0NL5lMm4muc2LWUIhLlPw_RTc8hoLUz25qx5Zfeitfd-5HZqjHrTw5b5amL8t4OrKJto_9fYD')
        time.sleep(1)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys('Outlook账户')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="i0118"]').send_keys('Outlook密码')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="KmsiCheckboxField"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()
        time.sleep(6)
        self.worksheet = xlrd.open_workbook('name_list.xlsx')
        self.sheet_names = self.worksheet.sheet_names()

    def get_department(self, staff_name):
        # 搜索人名
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/input').send_keys(
            staff_name)
        time.sleep(2)
        # 点击搜索
        self.driver.find_element(By.XPATH, '//*[@id="owaSearchBox"]/div/button/span').click()
        # 点击人名
        # self.driver.find_element_by_xpath(
        #     '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]').click()
        time.sleep(3)
        # 获取部门信息
        # department = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/div/div[2]/section/div/div/div/section/div/div/div/div/div[5]/div/div[1]/div/div/div/span')
        department = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/div/div/div/div[1]/header/div/div[2]/div[2]/span')
        print('姓名：{} 部门：{}'.format(staff_name, department.text))

    def run(self):
        for sheet_name in self.sheet_names:
            sheet = self.worksheet.sheet_by_name(sheet_name)
            cols = sheet.col_values(2)
            # print(cols[1:])
            for staff_name in cols[1:]:
                try:
                    self.get_department(staff_name)
                    self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/input').clear()
                    self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/button[1]/span').click()
                except Exception as e:
                    print('员工：{} 的数据异常，请手动搜索'.format(staff_name))
                    # print(e)
                    self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/input').clear()
                    self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/button[1]/span').click()


if __name__ == '__main__':
    spider = GetDepartment()
    spider.run()
