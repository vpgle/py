# -*- coding:gb18030 -*-
# /*
#  *���ֵ��д洢�б�
#  */ 

# �洢�����������Ϣ
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
    
# �������������

print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)


