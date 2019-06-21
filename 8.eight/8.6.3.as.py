# -*- coding: gb18030 -*-

print("使用as给函数指定别名")
print("from pizza import make_pizza as mp")
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
