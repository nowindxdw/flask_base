#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SelectField, SelectMultipleField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired(message=u"必填项")])
    # captcha = TextField('captcha', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)


class BaseUserForm(Form):
    email = StringField('email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired(message=u"必填项"),
                                                     Length(max=64, message=u"最长64字符")])
    role = SelectMultipleField('role', choices=[], validators=[DataRequired(message=u'必选项')])


class AddUserForm(BaseUserForm):
    pass


class ModifyUserForm(BaseUserForm):
    email = SelectField('email', validators=[DataRequired()], choices=[])
    password = PasswordField('Password', validators=[Length(max=64, message=u"最长64字符")])


class DelUserForm(Form):
    email = SelectField('email', validators=[DataRequired()], choices=[])


class ResetPassword(Form):
    password = PasswordField('Password', validators=[DataRequired(message=u"必填项"),
                                                     Length(max=64, message=u"最长64字符")])
