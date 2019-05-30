# -*- coding:gb18030 -*-

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Sarah's favorite language is "+
    favorite_languages['sarah'].title() +
    ".")

namelists = [
    'jen',
    'phil',
    'ly',
    'trump',
    ]
    
print(namelists)

for name in favorite_languages.keys():
    if name in namelists:
        print('\t' + name.title() + ", thank you !")
    else:
        print(name.title() + ', please take our poll!')
    
