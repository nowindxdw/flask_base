#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import logging
import time
from flask import Flask, request, g

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_redis import FlaskRedis
from sqlalchemy import create_engine
from flask_httpauth import HTTPTokenAuth

from apps import log

app = Flask(__name__)
app.config.from_object('config')


# log
log.init_log('log/tailor.log', level=logging.DEBUG)

# mysql
db = SQLAlchemy(app, session_options={"autoflush": False})

db.session.configure(bind=create_engine(
    app.config['SQLALCHEMY_BINDS']['base'],
    pool_recycle=1
))

# if bind more than one sqldb
#from sqlalchemy.orm import sessionmaker
# session bind for website
# Session = sessionmaker()
# websession = Session(
#     bind=create_engine(
#         app.config['SQLALCHEMY_BINDS']['website'],
#         pool_recycle=1
#     ), autocommit=False)

# redis connect
rs = FlaskRedis(app, socket_connect_timeout=0.5, socket_timeout=0.5)



@app.teardown_request
def teardown_request(exeception):
    db.session.close()
    # websession.close()


user_auth = HTTPTokenAuth()


@app.before_request
def before_request():
    local_time = time.time()
    trace_id = request.headers.get('Trace-Id')
    if trace_id:
        g.trace_id = trace_id
        print(" %s request receive trace_id : %s" % (local_time, trace_id))


@app.after_request
def after_request(response):
    local_time = time.time()
    if g.get("trace_id"):
        trace_id = g.get("Trace-Id")
        response.headers["Trace-Id"] = g.trace_id
        print(" %s response trace_id : %s" % (local_time, trace_id))
    return response



# Register User Blueprint
from apps.user import user
app.register_blueprint(user)

