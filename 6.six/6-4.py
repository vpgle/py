# -*- coding:gb18030 -*-
words = {
    'strip': 'ȥ���ַ�����β�Ŀո�',
    'for': 'ѭ�����',
    'sort': '����',
    'reverse': '����',
    'append': '���б�ĩβ����',
    }

print("strip: " + words['strip'])
print("\n")
print("for:")
print("\t" + words['for'])


print("\n")
print("sort:")
print("\t" + words['sort'])
print("\n")
print("reverse:")
print("\t" + words['reverse'])
print("\n")
print("append:")
print("\t" + words['append'])

words['lstrip'] = 'ȥ������˵Ŀո�'
words['rstrip'] = 'ȥ�����Ҷ˵Ŀո�'
words['in'] = '������ϵ'
words['not in'] = '������'
words['remove'] = '�Ƴ��б��е�Ԫ��'
words['pop'] = '�Ƴ��б�ĩβ��Ԫ��'

print("[] ��ʾ�б�")
print("words['pop'] = ['�Ƴ��б�ĩβ��Ԫ��']")
print("��ʱ����ӵľͲ������ֵ�����Ӽ�ֵ��")
print("�������ֵ������ֵΪ�б�ļ�ֵ�ԣ���for����д�ӡд�������ı�")
print(words)

for key, value in words.items():
    print("key is " + key)
    print("\tvalue is " + value) 

newwords = {}
newwords['pop(0)'] = ['�Ƴ�����Ϊ0��Ԫ��']
newwords['del'] = 'ɾ���б���ָ��������Ԫ��'

print(newwords)

for key in newwords.keys():
    print("newword key is " + key)

for value in newwords.values():
    print("newword value is " + str(value))

for key, value in newwords.items():
    print("newword key is " + key + ", newwords value is " + str(value))

for key, value in newwords.items():
    print(value)
