#!/usr/bin/env python
# 爬取搜狗首页图片
# 导入urlopen 函数
from urllib.request import urlopen
# 导入 BeautifulSoup 
from bs4 import BeautifulSoup as bf
# 导入urlretrieve函数，用于下载图片
from urllib.request import urlretrieve

html= urlopen("https://www.sogou.com/")

# 这里输出页面源码  
# html_text = bytes.decode(html.read())
# print(html_text)

obj=bf(html.read(),'html.parser')
# 从标签 head ,title中提取标题

content=obj.head.title

# 打印标题
print(content)

pic_info= obj.find_all('img')
# 分别打印每个图片的信息
for i in pic_info:
    print(i)


# 只提取logo图片的信息
# <img class="index-logo-src" height="129" hidefocus="true" src="//www.baidu.com/img/bd_logo1.png" usemap="#mp" width="270"/>
# logo_url=obj.find_all('img',class_="index-logo-src")


logo_url=obj.find_all('img',alt_="")

print(logo_url[0])
logo_url="https://www.sogou.com" + logo_url[0]['src']

print(logo_url)

# 可以用urllib.urlretrieve函数下载logo图片
urlretrieve(logo_url, 'logo.png')
