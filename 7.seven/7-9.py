# -*- coding: gb18030 -*-

sandwich_orders = ['tuna sandwich', 'pastrami sandwich',
    'funeral sandwich', 'pastrami sandwich', 
    'radish sandwich', 'pastrami sandwich']
finished_sandwiches = []

print("抱歉，pastrami sandwich 已卖完！")
while sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
    
    if 'pastrami sandwich' not in sandwich_orders:
        print("您要的三明治都有现货." + str(sandwich_orders))
        break

