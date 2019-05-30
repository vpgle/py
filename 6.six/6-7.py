# -*- coding:gb18030 -*-
# 6-1
shimaomin = {
    'first_name': 'maomin',
    'last_name': 'shi',
    'age': 30,
    'city': 'china',
    }

me = {
    'first_name': 'ly',
    'last_name': 'vivan',
    'age': 99,
    'city': 'earth',
    }
    
father = {
    'first_name': 'jesus',
    'last_name': 'god',
    'age': 'never',
    'city': 'anywhere',
    }

print("名： " + shimaomin['first_name'])
print("姓： " + shimaomin['last_name'])
print("年龄： " + str(shimaomin['age']))
print("在哪： " + shimaomin['city'])

for key, value in me.items():
    print(key + " is " + str(value).title())

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for key, value in father.items():
    print(key + " is " + value.title())
