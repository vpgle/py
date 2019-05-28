# -*- coding: gb18030 -*-

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

for num in range(1,3):
    print('*********************')
    
for language in sorted(set(favorite_languages.values())):
    print(language.title())
