# -*- coding: gb18030 -*-
import dog
# from dog import Dog
# class Dog():
    # """һ��ģ��С���ļ򵥳���"""

    # def __init__(self, name, age):
        # """��ʼ������name��age"""
        # self.name = name
        # self.age = age
    
    # def sit(self):
        # """ģ��С��������ʱ����"""
        # print(self.name.title() + " is now sitting.")

    # def roll_over(self):
        # """ģ��С��������ʱ���"""
        # print(self.name.title() + " rolled over!")

print("��������")
my_dog = dog.Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
