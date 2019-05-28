# coding=gb18030


cars = ['bmw',
        'audi',
        'toyota',
        'subaru']

print(cars)

print("注意，reverse()不是指按与字母顺序相反的顺序排列列表元素，")
print("而只是反转列表元素的排列顺序：")
cars.reverse()
print(cars)

print("方法reverse()永久性地修改列表元素的排列顺序，")
print("但可随时恢复到原来的排列顺序， ")
print("为此只需对列表再次调用reverse()即可。")


