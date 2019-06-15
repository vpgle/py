# -*- coding: gb18030 -*-

print("默认值")
print("函数定义: def describe_pet(pet_name, animal_type='dog'): ")
print("函数调用：describe_pet(pet_name='willie') ")

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')


print("**************************************************")
print("下面对这个函数的所有调用都可行：")
# 一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name = 'willie')

# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(animal_type = 'hamster', pet_name = 'harry')
