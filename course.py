# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:14:59 2020

@author: shubh
"""

'''
import requests
import json

d = {'q':'viollins and guitar','tbm':'isch'}
page = requests.get("https://google.com/search", params = d)
print(page.text[:2000])
print(page.url)
x = json.dump(page, sort_keys=True, inndent = 2)
print("-----------------------")
print(x)
'''

import requests 
import json


def rhyms(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {}
    params_diction['rel_rhy'] = word
    params_diction['max'] = '3'
    result = requests.get(baseurl ,params = params_diction)
    word_ds = result.json()
    return [d['word'] for d in word_ds]
print(rhyms("funny"))
    
