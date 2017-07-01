# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__, url_prefix='')

from . import articles, errors


@main.route('/test_post', methods=['POST'])
def test_post():
    print "test_post..form."
    print request.form
    print "test_post..data."
    print request.data
    print "test_post..json."
    print request.json
    return "ok"
