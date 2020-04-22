#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import time
from os import path
from lxml import etree
#百度top榜单
url = 'http://news.163.com/rank/'
#伪造浏览器请求header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
    'Host': 'news.163.com',
    'Referer': 'http://news.163.com/special/0001386F/rank_ent.html'
}
#提取关键字xpath
KEYWORD_XPATH = "//td[@class='red']/a/text()"
HREF_XPATH = "//td[@class='red']/a/@href"
#文件存储路径
d = path.dirname(__file__)
STORE_PATH = path.join("./topic/")

def store_new(path,data):
    #还需要注意文件的打开模式 w是写入，文件已存在的话就覆盖
    #要追加写入的话记得用 a模式打开
    with open(path, 'w') as fw:
        # 将字典转化为字符串
        # json_str = json.dumps(data)
        # fw.write(json_str)
        # 上面两句等同于下面这句
        json.dump(data,fw,ensure_ascii=False)


def request_url_get(url,decode_type="gb2312"):
    rep = requests.get(url=url, headers=headers)
    text = rep.content.decode(decode_type, "ignore")
    #print(text)
    html = etree.HTML(text,etree.HTMLParser())
    return html

def parse_detail_page(html):
    name = html.xpath(KEYWORD_XPATH)
    #print(name)
    href = html.xpath(HREF_XPATH)
    #print(href)
    list = []
    for i in range(0,len(name)):
        list.append({
            "title":name[i],
            "href":href[i]
        })
    return list

if __name__=='__main__':
    html = request_url_get(url)
    detail = parse_detail_page(html)
    print(detail)
    #写文件
    file_name = '163_topic_%s.txt' % time.strftime("%Y%m%d", time.localtime())
    store_new(STORE_PATH+file_name,detail)