from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_celery import Celery
import logging
from logging.handlers import RotatingFileHandler
from flask_cors import CORS
from flask_caching import Cache
from flask_socketio import SocketIO
from flask_debugtoolbar import DebugToolbarExtension

bootstrap = Bootstrap()     # 前端框架
mail = Mail()               # 邮件
moment = Moment()           # 时间格式
db = SQLAlchemy()           # 数据库
celery = Celery()           # 计划任务
login_manager = LoginManager()  # 登录管理器
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
cors = CORS()
cache = Cache()
socketio = SocketIO()
toolbar = DebugToolbarExtension()


def setup_log(app):
    """配置日志"""
    # 设置日志的记录等级
    logging.basicConfig(level=app.config['LOG_LEVEL'])  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler(
        app.config['LOG_FILENAME'],
        maxBytes=app.config['LOG_MAX_BYTES'],
        backupCount=app.config['LOG_BACKUP_COUNT']
    )
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter(app.config['LOG_FORMATTER'])
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def init_app(app):
    setup_log(app)
    toolbar.init_app(app)
    socketio.init_app(app)
    cache.init_app(app)
    cors.init_app(app)
    celery.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)