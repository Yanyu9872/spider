# import json
# from urllib.request import urlopen
#
# import requests
#
#
# class MmjpgSpider():
#     def __init__(self):
#         self.url = 'http://www.mmjpg.com/hot/'
#         self.headers = {
#             'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
#             'Referer': 'http://www.mmjpg.com/hot/',
#         }
#
#     def ImagemakeUrlList(self):
#         """构造url_list,并返回"""
#         return [self.url.format(i) for i in range(0, 21, 20)]
#
#     def getImage(self,url):
#         """发送请求获取响应，返回响应的文本内容"""
#         resp = requests.get(url, headers=self.headers)
#         return json.loads(resp.content.decode())
#
#
#     def imgDownload(self, item):
#         """写入一条数据"""
#         with open('./mmjpgs', 'a', encoding='utf-8') as f:
#             json.dump(item, f)
#
#
#     def run(self):
#         """爬虫运行逻辑"""
#         # 构造url_list
#         url_list = self.ImagemakeUrlList()
#         # 遍历url_lsit
#         for url in url_list:
#             # 发送请求获取响应dict响应内容
#
#             # 提取数据
#
#                 # 分别处理或保存一条数据
#
#
#
# if __name__ == '__main__':
#     spider = MmjpgSpider()
#     spider.run()

import requests
from bs4 import BeautifulSoup
import os

Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://www.mzitu.com'
}
Picreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://i.meizitu.net'
}


def get_page_name(url):#获得图集最大页数和名称
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    span = soup.findAll('span')
    title = soup.find('h2', class_="main-title")
    return span[10].text, title.text

def get_html(url):#获得页面html代码
    req = requests.get(url, headers=Hostreferer)
    html = req.text
    return html

def get_img_url(url, name):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    img_url = soup.find('img', alt= name)
    return img_url['src']

def save_img(img_url, count, name):
    req = requests.get(img_url, headers=Picreferer)
    with open(name+'/'+str(count)+'.jpg', 'wb') as f:
        f.write(req.content)

def main():
    old_url = "http://www.mzitu.com/123114"
    page, name = get_page_name(old_url)
    os.mkdir(name)
    for i in range(1, int(page)+1):
        url = old_url + "/" + str(i)
        img_url = get_img_url(url, name)
        #print(img_url)
        save_img(img_url, i, name)
        print('保存第' + str(i) + '张图片成功')
main()