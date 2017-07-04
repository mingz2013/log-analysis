# -*- coding:utf-8 -*-
'''
Created on 30/06/2017

@author: zhaojm
'''
import json

# 读取712配置文件
j_712_obj = json.load(open('config/712.json'))
table_config = j_712_obj['create_table_config']


def get_key_desc(play_mode, param_type):
    # print play_mode, param_type
    return table_config[play_mode]['paramType'][param_type]


def get_value_desc(play_mode, param_type, id):
    l = table_config[play_mode][param_type]
    for item in l:
        if item['id'] == id:
            return item['desc']
