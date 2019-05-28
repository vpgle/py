# -*- coding:gb18030 -*-

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
    
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("Sarah's favorite languages is " +
    favorite_languages['sarah'].title() +
    ".")

for name in favorite_languages.keys():
    print(name.title())

print("能正常显示中文部")

for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() +
            ",  I see your favorite language is " +
            favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("-----------------------------------------------")
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("     分隔符羞耻PLAY")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

for language in favorite_languages.values():
    print(language.title())
        
print("                                                ")
print("The following languages have been mentioned:")
for value  in set(favorite_languages.values()):
    print(value)
    # ~ print(language.title())    
