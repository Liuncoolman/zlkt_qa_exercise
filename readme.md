参考：
 - https://www.bilibili.com/video/BV17r4y1y7jJ
 - https://www.gitbook.com/book/wizardforcel/flask-extension-docs
 - https://v4.bootcss.com/docs/getting-started/introduction/


#### 一、 准备工作
- Python 3.x
- MySQL 5.x

#### 二、环境配置

2.1、安装virtualenv
  pip install virtualenv

2.2、创建虚拟环境envName
  virtualenv envName

2.3、激活虚拟环境()
  - macos source envName/bin/activate(activate路径)
  - windows cd  虚拟环境名称/Scripts/activate.bat

2.4、退出虚拟环境
  - macos deactivate
  - windows cd  虚拟环境名称/Scripts/deactivate.bat

2.5、指定虚拟环境的python版本

  > --no-site-packages 不包括系统包 --python=3.6版本 env 虚拟环境名称

  virtualenv --no-site-packages --python=3.6 env



#### 三、安装依赖库

```python
# 将当前环境下的安装包全部写入requirements.txt文件
pip freeze > requirements.txt
# 将requirements.txt文件里的包全部安装
pip install –r requirements.txt   

```

#### 四、数据库初始化

```python
flask db init
flask db migrate -m "初始化"
flask db upgrade

```

#### 五、启动
```python
python3 app.py

```
