from datetime import datetime
from flask import (Blueprint, jsonify, render_template, request, redirect,
                   url_for, flash, session)
from exts import db, mail
from flask_mail import Message
from models import EmailCaptchaModel, UserModel
from blueprints.forms import RegisterForm, LoginForm
import string
import random
from werkzeug.security import generate_password_hash


bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            session['user_id'] = request.form.get('email')
            return redirect(url_for('qa.index'))
        else:
            flash('账号或密码不匹配')
            return render_template('login.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # request.form 表单数据
        form = RegisterForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            email = form.email.data

            user = UserModel(username=username,
                             password=generate_password_hash(password),
                             email=email)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.login'))

        else:
            return render_template('register.html')


@bp.route('/get_captcha')
def get_captcha():
    # get post
    email = request.args.get('email')
    if (email):
        str = string.ascii_letters + string.digits  # 生成验证码库
        captcha = ''.join(random.sample(str, 4))
        # print("capcha:"+ capcha)
        model = EmailCaptchaModel.query.filter_by(email=email).first()
        if model:  # 邮箱存在，更新验证码
            model.captcha = captcha
            model.create_time = datetime.now()
            db.session.add(model)
            db.session.commit()

        else:  # 邮箱不存在，创建一条新的数据
            model = EmailCaptchaModel(email=email, captcha=captcha)
            db.session.add(model)
            db.session.commit()

        msg = Message(
            subject="知了问答测试邮件",
            #   sender="from@example.com",
            recipients=[email])
        msg.body = f"您的验证码是：{captcha}"
        # msg.html = "<b>您的验证码是</b>"
        mail.send(msg)
        return jsonify({'msg': '验证码已发送，请查收', 'code': 0})
    else:
        return jsonify({'msg': '邮箱缺失', 'code': -1})


@bp.route('/logout')
def logout():
    # 删除session中的user_id
    session.pop('user_id', None)
    return redirect(url_for('user.login'))

