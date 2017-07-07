# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import os

from flask import send_from_directory, render_template, make_response

from webapp.config import result_dir
from . import main


@main.route('/result/', methods=['GET'])
@main.route('/', methods=['GET'])
def index():
    result = []
    for top, dirs, nondirs in os.walk(result_dir):
        for filename in nondirs:
            d = {
                "filename": filename,
                "url": "/result/%s" % filename
            }
            result.append(d)

    return render_template("index.html", result=result)


@main.route('/result/<path:path>')
def send_json(path):
    # print "send_json", path
    response = make_response(send_from_directory(result_dir, path))
    response.headers['Content-type'] = "text/json; charset=utf-8"
    return response
