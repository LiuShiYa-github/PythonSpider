# 图片抓取
```text
说明:
    图片 音频 视频在计算机中均以二进制方式存储
实现:
    找到要抓取图片的URL地址
    向图片的URL地址发送请求,获取二进制响应内容(bytes)
    正常打开文件,将响应内容以web方式保存到本地
```

**图片抓取-爬取wallhaven.cc**

[代码](https://github.com/LiuShiYa-github/PythonSpider/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alxml%2Bxpath/SpiderWallhavenSelenimu.py)

![img_41.png](../Image/img_41.png)

![img_39.png](../Image/img_39.png)

![img_40.png](../Image/img_40.png)


# xpath语法解析

```text
定义:
    xpath即为XML路径语言,它是一种用来确定XML文档中某部分位置的语言,同样适用于HTML文档的检索

xpath 选取节点:
    只要涉及到条件,加[]://li[@class="xxx"] //li[2]
    只要获取属性值,加@://li[@class="xxx"] //li/@href
// : 从所有节点中查找(包括子节点和后代节点)
@ : 获取属性值

使用场景1(属性值作为条件): //div[@class="movie-item-info"]
使用场景2(直接获取属性值): //div[@class="movie-item-info"]/a/img/@src

使用xpath表达式匹配结果为两种情况:字符串和节点对象
    [1] xpath表达式的末尾为: /text() /@href 得到的列表中为"字符串"
    [2] 其他剩余所有情况得到的列表中均为"节点对象"
```


**xpath抓取QQ音乐热歌榜**

[代码](https://github.com/LiuShiYa-github/PythonSpider/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alxml%2Bxpath/xpathdemo.py)

![img_38.png](../Image/img_38.png)


# lxml+xpath解析抓取数据

**lxml解析库**
```text
安装:
    Ubuntu安装: sudo pip3 install lxml
    Windows安装: python -m pip install lxml
使用流程:
    导入模块: from lxml import etree
    创建解析对象: parse_html = etree.HTML(html)
    解析对象调用xpath: r_list = parse_html.xpath('xpath表达式')
注意:
    只要调用了xpath,则得到的数据类型一定为列表
```

**基于xpath抓取链家二手房**
```text
实现步骤:
    确认所抓取数据在响应内容中是否存在 -  存在
    分析URL地址规律
    写xpath表达式
    编写程序框架,完善程序
注意:
    在写xpath表达式时一切以响应内容为主
    页面中HTML为最终渲染完成之后的,和响应内容中的HTML不一定相同
```
[基于xpath抓取链家二手房](https://github.com/LiuShiYa-github/PythonSpider/blob/master/03%E7%AC%AC%E4%B8%89%E7%AB%A0%EF%BC%9Alxml%2Bxpath/LianHomeSpider.py "悬停显示")

![img_42.png](../Image/img_42.png)