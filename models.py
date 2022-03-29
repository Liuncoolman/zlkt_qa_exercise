from exts import db
from datetime import datetime


class EmailCaptchaModel(db.Model):
    __tablename__ = 'email_captcha'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False,
                      unique=False)  # unique 唯一
    captcha = db.Column(db.String(10), nullable=True)
    create_time = db.Column(db.DateTime,
                            default=datetime.now)  # datetime.now() 为运行的时间


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False,
                      unique=False)  # unique 唯一
    create_time = db.Column(db.DateTime,
                            default=datetime.now)  # datetime.now() 为运行的时间

class QuestionPublicModel(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_time = db.Column(db.DateTime,
                            default=datetime.now)  # datetime.now() 为运行的时间

    author = db.relationship('UserModel', backref="questions")


# flask db init
# flask db migrate -m "初始化email"
# flask db upgrade
