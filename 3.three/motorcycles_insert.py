# coding=gb18030


motorcycles = ['honda',
               'yamaha',
               'suzuki']
print(motorcycles)

print("这个示例中，值'ducati'被插入到了列表开头；方法insert()")
print("在索引0处添加空间，并将值'ducati'存储到这个地方。这种操作")
print("将列表中既有的每个元素都右移一个位置：")
motorcycles.insert(0, 'ducati')
print(motorcycles)
