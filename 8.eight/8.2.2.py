# -*- coding: gb18030 -*-

print("�ؼ���ʵ���Ǵ��ݸ�����������-ֵ��")
print("�����ǵ��÷���")
print("describe_pet(animal_type = 'hamster', pet_name = 'harry')")

def describe_pet(animal_type, pet_name):
    """��ʾ�������Ϣ"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type = 'hamster', pet_name = 'harry')