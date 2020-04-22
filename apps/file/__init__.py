#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint

file = Blueprint('file', __name__)

from apps.file import views
