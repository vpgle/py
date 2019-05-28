# -*- coding:gb18030 -*-

dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)    



for dimension in dimensions[:]:
    print(dimension)

for dimension in dimensions:
    print(dimension)
    
