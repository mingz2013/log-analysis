# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from . import main


@main.route('/', methods=['GET'])
def index():
    return "index"
