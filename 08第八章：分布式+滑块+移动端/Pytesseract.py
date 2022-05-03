#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: Pytesseract.py
@Time    : 2022/4/9 17:23
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 测试pytesseract识别图片
"""
import pytesseract
from PIL import Image

img = Image.open('./img.png')
result = pytesseract.image_to_string(img, lang='chi_sim')
print(result)
