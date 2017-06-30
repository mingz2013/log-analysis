# -*- coding:utf-8 -*-
'''
Created on 30/06/2017

@author: zhaojm
'''
import codecs
import json


def print_fenshu_tongji(l):
    print '====分数统计===='
    play_mode_result = {}

    for item in l:
        scores = item['scores']
        play_mode = item['play_mode:']
        if play_mode not in play_mode_result:
            play_mode_result[play_mode] = []
        play_mode_result[play_mode].append(scores)

    k_v_result = {}
    for (play_mode, scoress) in play_mode_result.items():
        k_v_result[play_mode] = {}
        for scores in scoress:
            for score in scores:
                if score not in k_v_result[play_mode]:
                    k_v_result[play_mode][score] = 0
                k_v_result[play_mode][score] += 1

    print json.dumps(k_v_result, ensure_ascii=False)
    with codecs.open('result/fenshu.json', encoding='utf-8', mode='wb') as f:
        json.dump(k_v_result, f, ensure_ascii=False)
    for (k, v) in k_v_result.items():
        print "---playMode:%s-----" % k
        for (kk, vv) in v.items():
            print '%s:%s' % (kk, vv)
