# -*- coding: gb18030 -*-

print("Ĭ��ֵ")
print("��������: def describe_pet(pet_name, animal_type='dog'): ")
print("�������ã�describe_pet(pet_name='willie') ")

def describe_pet(pet_name, animal_type='dog'):
    """��ʾ�������Ϣ"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')


print("**************************************************")
print("�����������������е��ö����У�")
# һ����ΪWillie��С��
describe_pet('willie')
describe_pet(pet_name = 'willie')

# һֻ��ΪHarry�Ĳ���
describe_pet('harry', 'hamster')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(animal_type = 'hamster', pet_name = 'harry')
