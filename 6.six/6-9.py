# -*- coding: gb18030 -*-

print("���ֵ��д洢�б�")
favorite_places = {
    'father': ['heaven', 'hunululu'],
    'maria': ['stable', 'saipan'],
    'egypt': ['cairo', 'london'],
    }
    
for name, place in favorite_places.items():
    print(name + " like ")
    for plac in place:
        print("\t" + plac.title())
