from datetime import datetime
from apps import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
#flask_login UserMixin implement all method need: is_authenticated	是登陆用户，返回TRUE；否则False
# is_active	是活动用户，返回TRUE；否则False
# is_anonymous	是匿名用户，返回TRUE；否则False
# get_id() 返回用户唯一标识，用unicode编码，即使是数字类型也要转换成unicode


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    login_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

