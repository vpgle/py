# -*- coding: gb18030 -*-

print("在字典中存储列表")
likenum = {
    'abort': [9, 3, 0,],
    'creepy': [7, 13, 1],
    'rebort': [5, 32, 111],
    'vivian': [99, 8],
    'ly': [1, 4, 3],
    }
print("abort like " + str(likenum['abort']))
print("creepy like " + str(likenum['creepy']))
print("rebort like " + str(likenum['rebort']))
print("vivian like " + str(likenum['vivian']))
print("ly like " + str(likenum['ly']))

for name, num in likenum.items():
    print(name + " like the nums: ")
    for number in num:
        print("\t" + str(number))

for name, num in likenum.items():
    print(name + " like " + str(num))
