# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from . import main
from flask import render_template, send_from_directory
from webapp.config import result_dir

@main.route('/', methods=['GET'])
def index():
    return "index"
    # return render_template("index.html")


@main.route('/result/<path:path>')
def send_json(path):
    print "send_json", path
    return send_from_directory(result_dir, path)
