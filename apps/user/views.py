#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import json
import os
from flask import render_template,request,g, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from apps import app,user_auth,login_manager,db
from apps.user import user
from apps.user import utils as user_utils
from apps.user.model import User
from apps.user.forms import RegistrationForm,LoginForm
# 这段代码是为了解决Python中中文输出出错而写，在Python2中适用，在Python3中已无效
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
# how to reload in python3 :
# import importlib
# importlib.reload(sys)


@user.route('/')
@user.route('/index')
@login_required
def index():
    return render_template("index.html", api_info=[], grow=[], summary=[])


@user.route('/logout')
@login_required
def login_out():
    """ logout """
    logout_user()
    return json.dumps({"status": 200,"msg":"Logged out successfully!"})


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


