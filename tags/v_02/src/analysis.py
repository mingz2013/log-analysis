# -*- coding:utf-8 -*-
'''
Created on 30/06/2017

@author: zhaojm
'''

import datetime
import os
import sys
import json

import file_utils
from plugins import fanxing_tongji
from plugins import fenshu_tongji
from plugins import wanfa_xuanze

reload(sys)
sys.setdefaultencoding("utf-8")
print "sys default encoding: ", sys.getdefaultencoding()

current_path = os.path.dirname(os.path.abspath(__file__))
source_path = os.path.join(current_path, "")
sys.path.append(source_path)


def get_list(file_name):
    print "load list start...%s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    # 从文件中读取到列表里
    l = file_utils.read_file_lines_to_list(file_name)
    print "load list...%s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    l2 = []
    for item in l:
        ps = "'" + item.strip() + "'"
        ps = eval(ps)
        l2.append(json.loads(ps))
    print "load list end...%s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    return l2


def do_day(date_now):
    file_name = 'data/analysis_%s.json' % date_now
    print 'file_name:%s' % file_name

    l = get_list(file_name)

    wanfa_result = wanfa_xuanze.print_wanfaxuanze(l)
    file_utils.write_obj_to_json_file(wanfa_result, 'result/wanfa_%s.json' % date_now)

    fanxing_result = fanxing_tongji.print_fanxing_tongji(l)
    file_utils.write_obj_to_json_file(fanxing_result, 'result/fanxing_%s.json' % date_now)

    fenshu_result = fenshu_tongji.print_fenshu_tongji(l)
    file_utils.write_obj_to_json_file(fenshu_result, 'result/fenshu_%s.json' % date_now)


def main():
    print "main now...%s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    day_list = [
        '2017_06_30'
    ]

    for date_now in day_list:
        do_day(date_now)

    print "main end now...%s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


if __name__ == '__main__':
    main()
