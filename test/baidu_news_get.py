#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import time
from os import path
from lxml import etree
#百度top榜单
#伪造浏览器请求header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
    'Host': 'www.baidu.com',
}
#提取关键字xpath
KEYWORD_XPATH = "//td[@class='keyword']/a[@class='list-title']/text()"
HREF_XPATH = "//td[@class='keyword']/a[@class='list-title']/@href"
#文件存储路径
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

def load(path):
    with open(path,'r') as f:
        data = json.load(f)
        return data
        
def request_url_get(url,decode_type="gb2312"):
    rep = requests.get(url=url, headers=headers)
    text = rep.content.decode(decode_type, "ignore")
    #print(text)
    html = etree.HTML(text,etree.HTMLParser())
    return html

def parse_detail_page(html):
    name = html.xpath(KEYWORD_XPATH)
    href = html.xpath(HREF_XPATH)
    list = []
    for i in range(0,len(name)):
        list.append({
            "title":name[i],
            "href":href[i]
        })
    return list

if __name__=='__main__':
    file_name = 'baidu_topic_%s.txt' % time.strftime("%Y%m%d", time.localtime())
    data = load(STORE_PATH+file_name)
    print(data[0])
    title = data[0].get("title")
    href = data[0].get("href")
    html = request_url_get(href)
    print(html)
    #detail = parse_detail_page(html)
    #print(detail)
    #写文件
    #file_name = 'baidu_topic_%s.txt' % time.strftime("%Y%m%d", time.localtime())
    #store_new(STORE_PATH+file_name,detail)