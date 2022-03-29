from flask import Blueprint, flash, render_template, g,request,redirect
from decorators import login_required
from models import QuestionPublicModel
from .forms import QuestionPublicForm
from exts import db

bp = Blueprint('qa', __name__, url_prefix='/')


@bp.route('/')
def index():
    if hasattr(g, 'user'):
        username = g.user.username
        print(f'username:{username}')

    return render_template('index.html')


@bp.route('/question/public', methods=['GET','POST'])
@login_required # 装饰器，做登录验证。
def question_public():
    if request.method == 'GET':
        return render_template('question_public.html')
    else:
        form = QuestionPublicForm(request.form)
        if form.validate():
            # save db
            title = request.form.get('title')
            content = request.form.get('content')
            model = QuestionPublicModel(title=title,content=content)
            user = g.get('user')
            model.author = user
            db.session.add(model)
            db.session.commit()

            return redirect('/')
        else:
            flash('请输入输入正确的标题和内容')
            return render_template('question_public.html')