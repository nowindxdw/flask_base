#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import json
import os
from flask import render_template,request,g, flash, redirect, url_for, jsonify
from apps import app,user_auth,db
from apps.user import user
from apps.user import utils as user_utils
from apps.user.model import User
from apps.user.forms import RegistrationForm,LoginForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
# 这段代码是为了解决Python中中文输出出错而写，在Python2中适用，在Python3中已无效
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
# how to reload in python3 :
# import importlib
# importlib.reload(sys)



@user.route('/')
@user.route('/index')
@user_auth.login_required
def index():
    return render_template("index.html", api_info=[], grow=[], summary=[])


@user.route('/logout')
@user_auth.login_required
def login_out():
    """ logout """
    g.user = None
    return json.dumps({"status": 200,"msg":"Logged out successfully!"})


@app.route('/register', methods=['GET', 'POST'])
def register():
    if g.get('user'):
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.get('user'):
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # # 生成token
        z_token = user.create_token(user.id)
        # print(z_token)
        # user["token"] = z_token
        g.user = user
        # print(g.user)
        return jsonify(token = z_token)
    return render_template('login.html', title='Sign In', form=form)


@user_auth.error_handler
def auth_failed():
    return redirect(url_for('login'))


@user_auth.verify_token
def verify_token(token):
    # print("token:%s" % token)
    # Config.SECRET_KEY:内部的私钥，这里写在配置信息里
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        # AuthFailed 自定义的异常类型
        flash('token不正确')
        return False
    except SignatureExpired:
        flash('token过期')
        return False
    # 校验通过返回True
    return True


