#!/usr/bin/env python
# 对于响应过慢的网站使用

import urllib2
response = urllib2.urlopen('http://www.baidu.com', timeout=10)
