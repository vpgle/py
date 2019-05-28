# -*- coding:gb18030 -*-

digits = list(range(1,11))

print('1.列表增加元素的两种方法')
print(digits)
print('①.digits.append(\'11\')')
digits.append(11)
print(digits)
print('②.digits.insert(-1, 12)')
digits.insert(-1, 12)
print(digits)
# print(digits.insert(-1, '12'))

print('2.列表修改元素值的方法')
print('digits[1] = 99')
digits[1] = 99
print(digits)

print('3.删除列表元素4种的方法')
print('①.del digits[5]')
del digits[5]
print(digits)
print('②.digits.remove(10)')
digits.remove(10)
print(digits)
print('③.digits.pop()')
digits.pop()
print(digits)
print('④.digits.pop(0)')
digits.pop(0)
print(digits)

print('&&&&&&&&&&&&&&&&&&&&我是害羞的分隔符&&&&&&&&&&&&&&&&&&&&&')
chars = 'e q u i p m e n t'.split()
print(chars)
print('4.排序3种方法')
print(digits)
print('sort()永久性修改列表元素顺序')
print('①.digits.sort()')
digits.sort()
print(digits)
print('①.digits.sort(reverse=True)')
digits.sort(reverse=True)
print(digits)


