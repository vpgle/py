# -*- coding: gb18030 -*-

print("λ��ʵ�Σ�˳�����Ҫ")




def describe_pet(animal_type, pet_name):
    """��ʾ�������Ϣ"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
