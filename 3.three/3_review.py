# -*- coding:gb18030 -*-

digits = list(range(1,11))

print('1.�б�����Ԫ�ص����ַ���')
print(digits)
print('��.digits.append(\'11\')')
digits.append(11)
print(digits)
print('��.digits.insert(-1, 12)')
digits.insert(-1, 12)
print(digits)
# print(digits.insert(-1, '12'))

print('2.�б��޸�Ԫ��ֵ�ķ���')
print('digits[1] = 99')
digits[1] = 99
print(digits)

print('3.ɾ���б�Ԫ��4�ֵķ���')
print('��.del digits[5]')
del digits[5]
print(digits)
print('��.digits.remove(10)')
digits.remove(10)
print(digits)
print('��.digits.pop()')
digits.pop()
print(digits)
print('��.digits.pop(0)')
digits.pop(0)
print(digits)

print('&&&&&&&&&&&&&&&&&&&&���Ǻ��ߵķָ���&&&&&&&&&&&&&&&&&&&&&')
chars = 'e q u i p m e n t'.split()
print(chars)
print('4.����3�ַ���')
print(digits)
print('sort()�������޸��б�Ԫ��˳��')
print('��.digits.sort()')
digits.sort()
print(digits)
print('��.digits.sort(reverse=True)')
digits.sort(reverse=True)
print(digits)


