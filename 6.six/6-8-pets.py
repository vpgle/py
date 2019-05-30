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

#pets = [pet_one, pet_two, pet_thr]
for pet in pet_one.keys():
    print(pet.title() + " is " + pet_one[pet])
    #print(pet_one[pet].title())
pets = [pet_one]
# for pet in pets:
    # print(type(pet))
    # for peta, master in pet.items():
        # print(peta + " is " + master)
        # print(pets[peta])
        # print("\n我是" + master + "科" + 
        # "主人是" + pets[peta]  + '! ')
