# -*- coding: gb18030 -*-

sandwich_orders = ['tuna sandwich',
    'funeral sandwich', 'radish sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich)
    finished_sandwiches.append(sandwich)

print(type(finished_sandwiches))
print(type(sandwich))
print("�����������ζ������ˣ�" + str(finished_sandwiches))
