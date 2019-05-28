# -*- coding: gb18030 -*-
# 6.3.2 遍历字典中的所有键

print("6.3.2 遍历字典中的所有键")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }


for name in favorite_languages.keys():
    print(name.title())

print("显式地使用方法keys()可让代码更容易理解，")
print("你可以选择这样做，但如果你愿意，也可省略它")
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

print("你还可以使用keys()确定某个人是否接受了调查 ")
print("下面的代码确定Erin是否接受了调查：")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


print()
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("6.3.3 按顺序遍历字典中的所有键")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
