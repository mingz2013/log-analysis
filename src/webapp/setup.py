# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import os
import sys

current_path = os.path.abspath(os.path.dirname(__file__))
source_path = os.path.join(current_path, "..")
sys.path.append(source_path)
# sys.path.append(os.path.join(source_path, ".."))
# sys.path.append(os.path.abspath('.'))

from webapp import create_app

print "************* CURRENT CONFIG MODE: ", os.getenv('demo.blog.config.mode')
mode = os.getenv('demo.blog.config.mode') or 'default'
if mode:
    mode = mode.lower()
    print 'current config mode: %s' % mode
app = create_app(mode)

if __name__ == '__main__':
    from default_encoding import init_encoding

    init_encoding()

    app.debug = True
    print "setup on http://0.0.0.0:5000"
    app.run(host='0.0.0.0', port=5000)
