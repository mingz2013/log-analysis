# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import render_template

from . import main


@main.app_errorhandler(403)
def error_403(error):
    # app.logger.error("403")
    return render_template('errors/403.html'), 403
    # return '403', 403


@main.app_errorhandler(404)
def error_404(error):
    # app.logger.error("404")
    return render_template('errors/404.html'), 404
    # return '404', 404


@main.app_errorhandler(405)
def error_405(error):
    # app.logger.error("405")
    return render_template('errors/405.html'), 405
    # return '405', 405


@main.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500
