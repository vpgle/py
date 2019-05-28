# coding=gb18030

numbers = list(range(1, 1000001))
print(sum(numbers))

print()
squares = [value**2 for value in range(1, 11)]
print(squares)


print([value**2 for value in range(1, 11)])
print("===============================================================")

for value in range(1, 6):
    print(value)

print([value for value in range(1, 11)])
