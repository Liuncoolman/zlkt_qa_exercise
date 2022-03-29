""" 自定义装饰器 """
from flask import g, redirect, url_for
from functools import wraps


# 没有登录回到登录页面
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if hasattr(g, 'user'):
            return func(*args, **kwargs)
        else:
            # 没有登录回到登录页面
            return redirect(url_for('user.login'))

    return wrapper
