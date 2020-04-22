#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import json
import os
from flask import render_template,request
from apps import app
from apps.user import user
from apps.user import utils as user_utils

# 这段代码是为了解决Python中中文输出出错而写，在Python2中适用，在Python3中已无效
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
# how to reload in python3 :
# import importlib
# importlib.reload(sys)


@user.route('/')
@user.route('/index')
def index():
    return render_template("index.html", api_info=[], grow=[], summary=[])








