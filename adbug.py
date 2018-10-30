import json
import requests
import time

"""
爬取adbug贷款相关字段
    抓取adbug.cn贷款相关
	# 创意名称
    title = scrapy.Field()
    # 尺寸大小
    type = scrapy.Field()
    # 广告开始投放时间
    start_time = scrapy.Field()
    # 广告最近抓取时间
    cur_time = scrapy.Field()
    # 素材链接
    url_link = scrapy.Field()
    # 投放信息
    info = scrapy.Field()
"""

url = "http://testapi.adbug.cn/api/v9/get/ads/search"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
data = {
    "wd":"贷款",
    "size": 100
}
res = requests.post(url, data=data, headers=headers)  #发送post请求
res_content = res.content.decode()      # 解码
res_dict = json.loads(res_content)      # 转换为json字典
res_data = res_dict["data"]             # 获取data数据

content_list = []
for data in res_data:
    item = {}
    item["title"] = data["title"]
    item["type"] = "%s" % data["width"] + "*" + "%s" % data["height"]
    item["start_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data["created_date"] / 1000))
    item["cur_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data["last_seen"] / 1000))
    item["url_link"] = data["attribute08"]
    item["info"] = data["publisher_full"]
    content_list.append(item)
    print(content_list)