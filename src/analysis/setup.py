# -*- coding:utf-8 -*-
'''
Created on 30/06/2017

@author: zhaojm
'''

import datetime
import os
import sys
import json


reload(sys)
sys.setdefaultencoding("utf-8")
print "sys default encoding: ", sys.getdefaultencoding()

current_path = os.path.dirname(os.path.abspath(__file__))
source_path = os.path.join(current_path, "..")
sys.path.append(source_path)

# sys.path.append(os.path.join(source_path, '..'))


from analysis import file_utils
from analysis.plugins import fanxing_tongji, fenshu_tongji, shijian_tongji, wanfa_tongji


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
    file_name = 'tmp/tmp_%s.json' % date_now
    print 'file_name:%s' % file_name

    l = get_list(file_name)

    wanfa_result = wanfa_tongji.print_wanfaxuanze(l)
    file_utils.write_obj_to_json_file(wanfa_result, 'result/wanfa_%s.json' % date_now)

    fanxing_result = fanxing_tongji.print_fanxing_tongji(l)
    file_utils.write_obj_to_json_file(fanxing_result, 'result/fanxing_%s.json' % date_now)

    fenshu_result = fenshu_tongji.print_fenshu_tongji(l)
    file_utils.write_obj_to_json_file(fenshu_result, 'result/fenshu_%s.json' % date_now)

    shijian_result = shijian_tongji.print_shijian_tongji(l)
    file_utils.write_obj_to_json_file(shijian_result, 'result/shijian_%s.json' % date_now)


def main():
    print "main now...%s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    # day_list = [
    #     # '2017_06_30',
    #     # '2017_07_01',
    #     # '2017_07_02'
    #     '2017_07_05'
    # ]

    # for date_now in day_list:
    #     do_day(date_now)

    date_lastday = datetime.datetime.now() + datetime.timedelta(days=-1)
    do_day(date_lastday.strftime('%Y_%m_%d'))

    print "main end now...%s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')


if __name__ == '__main__':
    main()
