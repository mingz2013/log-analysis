# -*- coding:utf-8 -*-
'''
Created on 30/06/2017

@author: zhaojm
'''
import json

# 读取712配置文件
j_712_obj = json.load(open('config/712.json'))
table_config_712 = j_712_obj['create_table_config']

j_711_obj = json.load(open('config/711.json'))
table_config_711 = j_712_obj['create_table_config']

table_config = {}

for (k, v) in table_config_711.items():
    if k not in table_config:
        table_config[k] = v
    else:
        print "conflict k", k

for (k, v) in table_config_712.items():
    if k not in table_config:
        table_config[k] = v
    else:
        print "conflict k", k


def get_key_desc(play_mode, param_type):
    # print play_mode, param_type
    return table_config[play_mode]['paramType'][param_type]


def get_value_desc(play_mode, param_type, id):
    l = table_config[play_mode][param_type]
    for item in l:
        if item['id'] == id:
            return item['desc']
