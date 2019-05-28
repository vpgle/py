# -*- coding: gb18030 -*-

alien_0 = {
    'color': 'green',
    'points': 5,
    }

print(alien_0['color'])
print(alien_0['points'])

print("6.2.1 访问字典中的值")
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

print("中文能正常显示不")

print("6.2.2 添加键值对")
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print('***************************************')
print("6.2.3 先创建一个空字典")
alien_0 = {}
alien_0['color'] = 'red'
alien_0['points'] = 25
print(alien_0)

print('***************************************')
print("6.2.4 修改字典中的值")
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + 


