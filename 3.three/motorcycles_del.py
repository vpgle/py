# coding=gb18030

motorcycles = ['honda',
               'yamaha',
               'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles.insert(0, 'wuling')
print(motorcycles)

print("append('dddd')  只能添加到末尾")
motorcycles.append('dddd')
print(motorcycles)

print("insert(1, '插入任意位置') 可以插入任意位置")
motorcycles.insert(2, '中文字符插入列表')
print(motorcycles)
