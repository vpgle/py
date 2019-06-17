# -*- coding: gb18030 -*-

def show_magicians(names):
    for name in names:
        print(name)

modify_name = []
def make_great(names):
    while names:
        current_name = names.pop()
        modify_name.append("the Great " + current_name)

names = ['al', 'dc', 'zz']

# 显示原列表
show_magicians(names)

# 显示添加"the Great"字样的列表

make_great(names[:])
show_magicians(modify_name)
