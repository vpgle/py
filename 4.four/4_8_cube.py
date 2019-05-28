# coding=gb18030

cubes = []
for cube in range(1,11):
    cube = cube ** 3
    print(cube)
    cubes.append(cube)
    
print()    
for cube in cubes:
    print(cube)    
