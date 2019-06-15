# -*- coding: gb18030 -*-

print("关键字实参是传递给函数的名称-值对")
print("以下是调用方法")
print("describe_pet(animal_type = 'hamster', pet_name = 'harry')")

def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type = 'hamster', pet_name = 'harry')
