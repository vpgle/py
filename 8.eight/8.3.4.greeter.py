# -*- coding: gb18030 -*-

print('8.3.4.greeter.py')

def get_formatted_name(first_name, last_name):
    """�������������"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# ����һ������ѭ����

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

