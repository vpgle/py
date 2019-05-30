# -*- coding: gb18030 -*-

print("在字典中存储列表")
favorite_places = {
    'father': ['heaven', 'hunululu'],
    'maria': ['stable', 'saipan'],
    'egypt': ['cairo', 'london'],
    }
    
for name, place in favorite_places.items():
    print(name + " like ")
    for plac in place:
        print("\t" + plac.title())
