# -*- coding:gb18030 -*-
words = {
    'strip': '去除字符串首尾的空格',
    'for': '循环语句',
    'sort': '排序',
    'reverse': '倒序',
    'append': '在列表末尾增加',
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

words['lstrip'] = '去除最左端的空格'
words['rstrip'] = '去除最右端的空格'
words['in'] = '包含关系'
words['not in'] = '不包含'
words['remove'] = '移除列表中的元素'
words['pop'] = '移除列表末尾的元素'

print("[] 表示列表")
print("words['pop'] = ['移除列表末尾的元素']")
print("这时你添加的就不是在字典中添加键值对")
print("而是在字典中添加值为列表的键值对，在for语句中打印写法有所改变")
print(words)

for key, value in words.items():
    print("key is " + key)
    print("\tvalue is " + value) 

newwords = {}
newwords['pop(0)'] = ['移除索引为0的元素']
newwords['del'] = '删除列表中指定索引的元素'

print(newwords)

for key in newwords.keys():
    print("newword key is " + key)

for value in newwords.values():
    print("newword value is " + str(value))

for key, value in newwords.items():
    print("newword key is " + key + ", newwords value is " + str(value))

for key, value in newwords.items():
    print(value)
