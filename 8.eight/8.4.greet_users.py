# -*- coding: gb18030 -*-

def greet_users(names):
    """���б��е�ÿλ�û��������򵥵��ʺ�"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
