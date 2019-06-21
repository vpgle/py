# -*- coding: gb18030 -*-

print("使用as给模块指定别名")
print("import pizza as p")
import pizza as p


p.make_pizza(99, 'pepperoni')
p.make_pizza(666, 'mushrooms', 'green peppers', 'extra cheese')

