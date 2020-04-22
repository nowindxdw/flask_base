#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# 
# __author__ = 'QeeYou'
# __file__ = 'utils.py'
# __date__ = '2017/10/20 10:48'

import functools
import traceback
import json


def load(path):
    with open(path, 'r') as f:
        data = json.load(f)
        return data


def store_file(path,data):
    #还需要注意文件的打开模式 w是写入，文件已存在的话就覆盖
    #要追加写入的话记得用 a模式打开
    with open(path, 'w') as fw:
        # 将字典转化为字符串
        # json_str = json.dumps(data)
        # fw.write(json_str)
        # 上面两句等同于下面这句
        json.dump(data,fw,ensure_ascii=False)