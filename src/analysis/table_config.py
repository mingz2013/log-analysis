# -*- coding:utf-8 -*-
'''
Created on 30/06/2017

@author: zhaojm
'''
import json

# 读取712配置文件
__j_712_obj = json.load(open('config/712.json'))
__table_config_712 = __j_712_obj['create_table_config']

__j_711_obj = json.load(open('config/711.json'))
__table_config_711 = __j_712_obj['create_table_config']

__table_config = {}

for (k, v) in __table_config_711.items():
    if k not in __table_config:
        print k
        __table_config[k] = v
    else:
        print "conflict k", k

for (k, v) in __table_config_712.items():
    if k not in __table_config:
        print k
        __table_config[k] = v
    else:
        print "conflict k", k

print __table_config


def get_key_desc(play_mode, param_type):
    # print play_mode, param_type
    return __table_config[play_mode]['paramType'][param_type]


def get_value_desc(play_mode, param_type, id):
    l = __table_config[play_mode][param_type]
    for item in l:
        if item['id'] == id:
            return item['desc']
