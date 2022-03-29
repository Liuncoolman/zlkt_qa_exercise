# coding: utf8

# 从flask框架中导入Flask类
from flask import Flask, session, g
from flask_migrate import Migrate
from exts import db, mail
# from blueprints import qa_bp, user_bp
from blueprints.qa import bp as qa_bp
from blueprints.user import bp as user_bp
from models import UserModel

# 传入__name__初始化一个Flask实例
app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)
db.init_app(app)
mail.init_app(app)
app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)

migrate = Migrate(app, db)


# 网络请求钩子
@app.before_request
def before_request():
    email = session.get('user_id')
    if email:
        user = UserModel.query.filter_by(email=email).first()
        if user:
            g.user = user  # g，全局变量
        else:
            g.user = None


# 上下文处理器
# 请求-> before_request -> 执行视图函数 -> 执行render_template -> context_processor
@app.context_processor
def context_processor():
    if hasattr(g, 'user'):
        return {'user': g.user}
    else:
        return {}


if __name__ == '__main__':

    # 创建数据库引擎
    # app.run(host='127.0.0.1', port='5000')
    app.run()
