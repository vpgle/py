# -*- coding:gb18030 -*-
# 宠物列表
import json
pet_one = {
    'pet': 'dog',
    'master': 'vincent',
    }
    
pet_two = {
    'pet': 'cat',
    'master': 'trump',
    }
    
pet_thr = {
    'pet': 'fish',
    'master': 'Reagan',
    }

pets = [pet_one, pet_two, pet_thr]

for pet in pets:
    print()
    for peta, master in pet.items():
        print(peta + " is " + master)

