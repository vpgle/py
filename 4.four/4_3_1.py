
for num in list(range(1,6)):
    print(num)
    
nums = list(range(1, 11, 2))
print(nums)

print(list(range(2, 11, 2)))
squares = []
for square in range(1, 11):
    square = square ** 2
    print(square)
    squares.append(square)

print(squares)

for square in squares:
    print(square)

print(min(squares))
print(max(squares))
print(sum(squares))
