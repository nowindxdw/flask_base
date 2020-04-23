from datetime import datetime
from apps import app,db
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
#token认证模式



class User(db.Model):
    __tablename__ = 'user'
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

    # 生成token
    @staticmethod
    def create_token(user_id):
        """
        生成token
        :param user_id: 用户id
        :return:
        """
        # 第一个参数是内部的私钥，这里写在配置信息里，如果只是测试可以写死
        # 第二个参数是有效期（秒）
        s = Serializer(app.config['SECRET_KEY'], expires_in=app.config['TOKEN_EXPIRATION'])
        # 接收用户id转换与编码
        token = s.dumps({"id": user_id}).decode('ascii')
        return token

