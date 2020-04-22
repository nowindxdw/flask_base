#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import json
import os
from flask import render_template,request
from apps import app
from apps.file import file
from apps.file import utils as file_utils

# 这段代码是为了解决Python中中文输出出错而写，在Python2中适用，在Python3中已无效
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
# how to reload in python3 :
# import importlib
# importlib.reload(sys)


@file.route("/file/file_list", methods=['GET', 'POST'])
def file_list():
    """ file管理页面 """
    data = []
    for i in os.listdir(os.path.join(app.config.get('BASEDIR'),'test')):
        print(i)
        data.append(i)
    return render_template('file/user_list.html',files=data)


@file.route("/file/mange_json", methods=['GET', 'POST'])
def mange_json():
    """ json管理页面 """
    return render_template('filejson_manage_index.html')


@file.route("/file/json_list", methods=['GET', 'POST'])
def json_list():
    """ json管理页面 """
    data = []
    for i in os.listdir(os.path.join(app.config.get('BASEDIR'),'test/material')):
        #print i
        data.append(i)
    return render_template('file/json_list.html',files=data)


@file.route('/user/json_edit', methods=['GET', 'POST'])
def json_edit():
    """ 编辑json """
    op = request.values.get('op', 'edit')
    user_id = request.values.get('user_id', '')
    if request.method == 'GET':
        dir_path = os.path.join(app.config.get('BASEDIR'),'test/material')
        file_path = os.path.join(dir_path, user_id)
        content = file_utils.load(file_path)
        if not content:
            return render_template('file/json_edit.html', title='修改json', error='json不存在')
        id = 1
        data = []
        for c in content:
            data.append({
                "id" : c.get('id') if c.get('id') else id,
                "key": c.get('key'),
                "val": c.get('val')
            })
            id = id +1
        print(data)
        return render_template('file/json_edit.html', title='修改json',
                               op='edit', file=user_id, content=data)

    else:
        data = request.values.get('data')
        print(data)
        data = json.loads(data)
        if op == 'edit':
            dir_path = os.path.join(app.config.get('BASEDIR'),'test/material')
            file_path = os.path.join(dir_path, user_id)
            file_utils.store_file(file_path, data)
        return json.dumps({'status': 0, 'msg': 'file修改成功'})