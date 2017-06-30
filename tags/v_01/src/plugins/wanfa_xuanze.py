# -*- coding:utf-8 -*-
'''
Created on 30/06/2017

@author: zhaojm
'''

import codecs
import json

import table_config


def print_wanfaxuanze(l):
    print "======玩法统计======="
    # 通过列表数据 打印玩法统计结果

    # 用playmode区分item_params
    play_mode_result = {}
    for obj in l:
        item_params = obj['item_params']
        play_mode = obj['play_mode:']
        if play_mode not in play_mode_result:
            play_mode_result[play_mode] = []
        play_mode_result[play_mode].append(item_params)

    # 解析item_params
    k_v_result = {}
    for (k, v) in play_mode_result.items():
        k_v_result[k] = {}
        for item_params in v:
            for (kk, vv) in item_params.items():
                if kk == u'wanFa':
                    for wan_fa in vv:
                        if wan_fa not in k_v_result[k]:
                            k_v_result[k][wan_fa] = 0
                        k_v_result[k][wan_fa] += 1
                else:
                    # new_key = '%s_%s' % (kk, vv)
                    new_key = '%s_%s' % (table_config.get_key_desc(k, kk), table_config.get_value_desc(k, kk, vv))
                    if new_key not in k_v_result[k]:
                        k_v_result[k][new_key] = 0
                    k_v_result[k][new_key] += 1

    print json.dumps(k_v_result, ensure_ascii=False)

    for (k, v) in k_v_result.items():
        print "---playMode:%s-----" % k
        for (kk, vv) in v.items():
            print '%s:%s' % (kk, vv)
