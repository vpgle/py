# -*- coding: gb18030 -*-

print('8.3.1.formatted_name.py')

def get_formatted_name(first_name, last_name):
    """�������������"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
