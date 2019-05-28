# coding=gb18030

motorcycles = ['honda',
               'yamaha',
               'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

print("方法pop()是怎么起作用的呢？假设列表中的摩托车是按购买时间存储的，")
print("就可使用方法pop()打印一条消息，指出最后购买的是那款摩托车：")

motorcycles.append('suzuki')
print(motorcycles)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

print(motorcycles)

motorcycles.append('suzuki')
print(motorcycles)

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a '+ first_owned.title() + '.')
print(motorcycles)

print("如果你不确定该使用del语句还是pop()方法，下面是一个简单的判断标准：")
print("如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句")
print("如果你要在删除元素后还能继续使用它，就使用方法pop()")

print("===============================我是华丽的分割线=-===============================")
motorcycles = ['honda',
               'yamaha',
               'suzuki',
               'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

print("===============================我是华丽的分割线=-===============================")

print("在末尾添加'ducati'")
motorcycles.append('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")


print("方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，")
print("就需要使用循环来判断是否删除了所有这样的值。你将在第7章学习如何这样做")






