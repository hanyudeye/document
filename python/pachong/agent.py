#!/usr/bin/env python

# 设置请求身份agent

import urllib

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
values = {'username' : 'cqc',  'password' : 'XXXX' }  
headers = { 'User-Agent' : user_agent }  
data = urllib.urlencode(values)  
request = urllib.Request(url, data, headers)  
response = urllib.urlopen(request)  
page = response.read() 


# 设置反盗链 Referer
# headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  , 'Referer':'http://www.zhihu.com/articles' }
