# -*- coding: gb18030 -*-

my_foods = ['pizza',
            'falafel',
            'carrot cake']
friend_foods = my_foods

print("============================")
print('我是美食分割线')
print("===================")
my_foods.append('cannoli')
friend_foods.append('ice cream')
for my_food in my_foods:
    print(my_food)

for friend_food in friend_foods:
    print(friend_food)    

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("============================")
print('我是美食分割线')
print("===================")
