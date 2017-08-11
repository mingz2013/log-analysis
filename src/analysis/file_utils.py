# -*- coding:utf-8 -*-
'''
Created on 30/06/2017

@author: zhaojm
'''

import json
import codecs


def get_file_txt(file_name):
    with codecs.open(file_name, encoding='utf-8') as f:
        txt = f.read()
        return txt


def read_file_lines_to_list(file_name):
    with codecs.open(file_name, encoding='utf-8') as f:
        return f.readlines()


def write_obj_to_json_file(obj, file_name):
    with codecs.open(file_name, encoding='utf-8', mode='wb') as f:
        json.dump(obj, f, sort_keys=True, ensure_ascii=False, indent=2)

