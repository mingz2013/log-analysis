# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from . import main
from flask import render_template


@main.route('/', methods=['GET'])
def index():
    # return "index"
    return render_template("index.html")
