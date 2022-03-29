DEBUG = True

# SECRET_KEY
SECRET_KEY = 'abcd'

# 数据库配置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlkt_qa'
USERNAME = 'root'
PASSWORD = '12345678'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

# 发送邮件配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = 'liun867@qq.com'
MAIL_PASSWORD = 'buyrctklvmmgbheb'
MAIL_DEFAULT_SENDER = 'liun867@qq.com'
# MAIL_MAX_EMAILS = None
# MAIL_SUPPRESS_SEND = app.testing
# MAIL_ASCII_ATTACHMENTS = False
