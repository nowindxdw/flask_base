#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import time
from os import path
from lxml import etree
#163top榜单
#伪造浏览器请求header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
    'Host': 'home.163.com',
}

FILE_NAME_PRE = '163_topic'
OUT_NAME_PRE = '163_news'
#提取关键字xpath
TEXT_XPATH = "//div[@class='post_text']/p/text()"

TEXT2_XPATH = "//div[@class='content']/p/text()"
#文件存储路径
READ_PATH = path.join("./topic/")
STORE_PATH = path.join("./news/")

def store_new(path,data):
    #还需要注意文件的打开模式 w是写入，文件已存在的话就覆盖
    #要追加写入的话记得用 a模式打开
    with open(path, 'w',encoding='utf-8') as fw:
        # 将字典转化为字符串
        # json_str = json.dumps(data)
        # fw.write(json_str)
        # 上面两句等同于下面这句
        json.dump(data,fw,ensure_ascii=False)

def load(path):
    with open(path,'r') as f:
        data = json.load(f)
        return data
        
def request_url_get(url,host,decode_type="gb2312"):
    headers["Host"] = host
    rep = requests.get(url=url, headers=headers)
    text = rep.content.decode(decode_type, "ignore")
    #print(text)
    html = etree.HTML(text,etree.HTMLParser())
    return html

def parse_detail_page(html):
    text = html.xpath(TEXT_XPATH)
    #print(text)
    if not text:
        text = html.xpath(TEXT2_XPATH)
    str = ""
    text_str = str.join(text)
    return text_str.replace("\xa0","")

    
def write_all(data):
    filter_data = []
    for d in data:
        title = d.get("title")
        href = d.get("href")
        print(title)
        print(href)
        host = href.split("://")[1].split("163.com")[0] + "163.com"
        html = request_url_get(href,host)
        detail = parse_detail_page(html)
        print(detail)
        if detail:
            news = detail
            filter_data.append({
                "title":title,
                "href":href,
                "news":news
                })
    #写文件
    file_name = '%s_%s.txt' % (OUT_NAME_PRE,time.strftime("%Y%m%d", time.localtime()))
    store_new(STORE_PATH+file_name,filter_data)
 
def write_for_test(data):
    d = data[9]
    title = d.get("title")
    href = d.get("href")
    print(title)
    print(href)
    host = href.split("http://")[1].split("163.com")[0] + "163.com"
    print(host)
    html = request_url_get(href,host)
    detail = parse_detail_page(html)
    print(detail) 

if __name__=='__main__':
    file_name = '%s_%s.txt' % (FILE_NAME_PRE ,time.strftime("%Y%m%d", time.localtime()))
    data = load(READ_PATH+file_name)
    write_all(data)
    
    
