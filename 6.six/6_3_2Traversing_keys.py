# -*- coding: gb18030 -*-
# 6.3.2 �����ֵ��е����м�

print("6.3.2 �����ֵ��е����м�")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }


for name in favorite_languages.keys():
    print(name.title())

print("��ʽ��ʹ�÷���keys()���ô����������⣬")
print("�����ѡ�����������������Ը�⣬Ҳ��ʡ����")
for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    print(favorite_languages[name].title())
    
    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " + 
            favorite_languages[name].title() + "!")

for name in favorite_languages.keys():
    print("------------------------------")
    print(favorite_languages[name].title())
    print(favorite_languages[name])

print("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
print("\t" + favorite_languages['phil'])

print("�㻹����ʹ��keys()ȷ��ĳ�����Ƿ�����˵��� ")
print("����Ĵ���ȷ��Erin�Ƿ�����˵��飺")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


print()
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("6.3.3 ��˳������ֵ��е����м�")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
