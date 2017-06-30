# -*- coding:utf-8 -*-
'''
Created on 30/06/2017

@author: zhaojm
'''

import codecs
import datetime

import fanxing_tongji
import fenshu_tongji
import wanfa_xuanze


def get_list(file_name):
    # 从文件中读取到列表里
    with codecs.open(file_name, encoding='utf-8') as f:
        txt = f.read()
        l = txt.strip().split('\n')
        l2 = [eval(str(item)) for item in l]
        return l2


def main():
    print "main now...%s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    file_name = 'data/analysis_2017_06_27.json'
    print 'file_name:%s' % file_name
    l = get_list(file_name)

    # print "load list now...%s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    wanfa_xuanze.print_wanfaxuanze(l)
    fanxing_tongji.print_fanxing_tongji(l)
    fenshu_tongji.print_fenshu_tongji(l)

    print "main end now...%s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


if __name__ == '__main__':
    import sys

    reload(sys)
    sys.setdefaultencoding("utf-8")
    print "sys default encoding: ", sys.getdefaultencoding()

    main()
