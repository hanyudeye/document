#!/usr/bin/env python
# 爬取百度首页
# 导入urlopen 函数
from urllib.request import urlopen
# 导入 BeautifulSoup 
from bs4 import BeautifulSoup as bf

html= urlopen("https://www.baidu.com/")

# 这里输出页面源码  
# html_text = bytes.decode(html.read())
# print(html_text)

obj=bf(html.read(),'html.parser')

# <html>
# <head>
# 	<script>
# 		location.replace(location.href.replace("https://","http://"));
# 	</script>
# </head>
# <body>
# 	<noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>
# </body>
# </html>

# 从标签 head ,script 中提取 内容

content=obj.head.script

# 打印内容
print(content)
