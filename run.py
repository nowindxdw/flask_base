#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 因为通常结合ngnix部署到服务端（一并打包到docker），此处只做本地调试使用，故无需将端口debugt放入配置文件
from apps import app

if __name__ == '__main__':
    app.run("0.0.0.0", 8008, debug=True)
