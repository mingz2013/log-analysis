# -*- coding:utf-8 -*-
'''
Created on 30/06/2017

@author: zhaojm
'''

import json

import table_config


def print_wanfaxuanze(l):
    print "======玩法统计======="
    result = {}
    for item in l:
        item_params = item['item_params']
        play_mode = item['play_mode:']
        if play_mode not in result:
            result[play_mode] = {}
        for (kk, vv) in item_params.items():
            if kk == u'wanFa':
                for wan_fa in vv:
                    if wan_fa not in result[play_mode]:
                        result[play_mode][wan_fa] = 0
                    result[play_mode][wan_fa] += 1
            else:
                # new_key = '%s_%s' % (kk, vv)
                new_key = '%s_%s' % (
                    table_config.get_key_desc(play_mode, kk), table_config.get_value_desc(play_mode, kk, vv))
                if new_key not in result[play_mode]:
                    result[play_mode][new_key] = 0
                result[play_mode][new_key] += 1
    print json.dumps(result, sort_keys=True, ensure_ascii=False)

    return result
