# -*- coding: gb18030 -*-

print("导入模块中的所有函数")
print("from pizza import *")
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print("最佳的做法是，要么只导入你需要使用的函数，" 
    +  "\n要么导入整个模块并使用句点表示法。"
    +  "\n这能让代码更清晰，更容易阅读和理解。"
    +  "\n这里之所以介绍这种导入方法，只是想让你在阅读别人编写的代码时，"
    +  "\n如果遇到类似下面的import语句，能够理解它们："
    +  "from module_name import *")
