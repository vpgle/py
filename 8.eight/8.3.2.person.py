# -*- coding: gb18030 -*-

print('8.3.2.person.py')

def build_person(first_name, last_name):
    """����һ���ֵ䣬���а����й�һ���˵���Ϣ"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
