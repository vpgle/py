# -*- coding: gb18030 -*-

sandwich_orders = ['tuna sandwich', 'pastrami sandwich',
    'funeral sandwich', 'pastrami sandwich', 
    'radish sandwich', 'pastrami sandwich']
finished_sandwiches = []

print("��Ǹ��pastrami sandwich �����꣡")
while sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
    
    if 'pastrami sandwich' not in sandwich_orders:
        print("��Ҫ�������ζ����ֻ�." + str(sandwich_orders))
        break

