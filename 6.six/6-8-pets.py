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

#pets = [pet_one, pet_two, pet_thr]
pets = [pet_one]
for pet in pets:
    for peta, master in pet.items():
        print("\n����" + peta + "��")
        print("������" + master  + '! ')
