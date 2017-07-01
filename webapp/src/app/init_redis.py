# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import os
import sys

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath('.'))
# from app import create_app, db
#
# print "************* CURRENT CONFIG MODE: ", os.getenv('demo.blog.config.mode')
# mode = os.getenv('demo.blog.config.mode') or 'default'
# if mode:
#     mode = mode.lower()
#     print 'current config mode: %s' % mode
# app = create_app(mode)

if __name__ == '__main__':
    from default_encoding import init_encoding

    init_encoding()

    # with app.app_context():
    #     db.create_all()
    from app.dbredis import RedisClient

    RedisClient.init_redis()
