# coding=gb18030


cars = ['bmw',
        'audi',
        'toyota',
        'subaru']

print("Here is the original list:")
print(cars)

print("=\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the orignial list again:")
print(cars)

print("扭向临时排序：")
print("=\nHere is the sorted list:")
new_sort = sorted(cars,reverse=True)
print(new_sort)
print(sorted(cars,reverse=True))
