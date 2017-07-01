# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


def register_logging(app):
    import logging
    from logging.handlers import RotatingFileHandler
    # 内部日志
    rotating_handler1 = RotatingFileHandler('logs/info.log', maxBytes=1 * 1024 * 1024, backupCount=5)
    rotating_handler2 = RotatingFileHandler('logs/error.log', maxBytes=1 * 1024 * 1024, backupCount=2)
    formatter1 = logging.Formatter("-" * 100 +
                                   '\n %(asctime)s %(levelname)s - '
                                   'in %(funcName)s [%(filename)s:%(lineno)d]:\n %(message)s')
    rotating_handler1.setFormatter(formatter1)
    rotating_handler2.setFormatter(formatter1)
    app.logger.addHandler(rotating_handler1)
    app.logger.addHandler(rotating_handler2)
    app.logger.setLevel(logging.INFO)
    rotating_handler2.setLevel(logging.ERROR)
    if app.config.get("DEBUG"):
        # app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.DEBUG)
    pass


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_mode):
    from flask import Flask
    app = Flask(__name__)
    from config import config_dict
    app.config.from_object(config_dict[config_mode])
    config_dict[config_mode].init_app(app)
    app.config_mode = config_mode

    register_logging(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
