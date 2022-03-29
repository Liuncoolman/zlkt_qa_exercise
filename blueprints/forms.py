import wtforms
from wtforms.validators import email, length, EqualTo
from models import EmailCaptchaModel, UserModel
from werkzeug.security import check_password_hash


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3, max=20)])
    password = wtforms.StringField(validators=[length(min=6, max=20)])
    password_confirm = wtforms.StringField(validators=[EqualTo('password')])
    email = wtforms.StringField(validators=[email()])
    captcha = wtforms.StringField(validators=[length(min=4, max=4)])

    # 重写方法自定义验证，validate_字段名
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data

        emailCatchaModel = EmailCaptchaModel.query.filter_by(
            email=email).first()
        if not emailCatchaModel or emailCatchaModel.captcha.lower(
        ) != captcha.lower():
            raise wtforms.ValidationError('验证码输入有误')

    def validate_email(self, field):
        email = field.data

        userModel = UserModel.query.filter_by(email=email).first()
        if userModel:
            raise wtforms.ValidationError('邮箱已存在')


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(min=6, max=20)])

    # 重写方法自定义验证，validate_字段名
    def validate_password(self, field):
        password = field.data
        email = self.email.data
        userModel = UserModel.query.filter_by(email=email).first()
        if not (userModel and check_password_hash(pwhash=userModel.password,
                                                  password=password)):
            raise wtforms.ValidationError('账号或密码输入有误')

class QuestionPublicForm(wtforms.Form):
    title = wtforms.StringField(validators=[length(min=5,max=50)])
    content = wtforms.StringField(validators=[length(min=5)])
