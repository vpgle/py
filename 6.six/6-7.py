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

print("���� " + shimaomin['first_name'])
print("�գ� " + shimaomin['last_name'])
print("���䣺 " + str(shimaomin['age']))
print("���ģ� " + shimaomin['city'])

for key, value in me.items():
    print(key + " is " + str(value).title())

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for key, value in father.items():
    print(key + " is " + value.title())
