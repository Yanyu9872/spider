import urllib.request

import requests


url = 'http://i.meizitu.net/2018/08/24c05.jpg'
headers = {
            'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Referer': 'http://m.mzitu.com/hot/'}

# 构造请求
request = urllib.request.Request(url, headers=headers)
#　获取响应
resp = urllib.request.urlopen(request)

#　提取数据
result = resp.read()

# 保存数据
with open('mm.jpg','wb') as f:
    f.write(result)