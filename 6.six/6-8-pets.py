# -*- coding:gb18030 -*-
# �����б�
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

print(type(pet_one))
pets = ['pet_one', 'pet_two', 'pet_thr']
for pet in pets:
    print("\t" + pet)
    print(type(pet))
    for pet_info in pet.items():
        print("����" + pet_info['pet'] + "��")
        print("\n������" + pet_into['master']  + '! ')
