# -*- coding: gb18030 -*-

alien_0 = {
    'color': 'green',
    'points': 5,
    }

print(alien_0['color'])
print(alien_0['points'])

print("6.2.1 �����ֵ��е�ֵ")
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

print("������������ʾ��")

print("6.2.2 ��Ӽ�ֵ��")
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print('***************************************')
print("6.2.3 �ȴ���һ�����ֵ�")
alien_0 = {}
alien_0['color'] = 'red'
alien_0['points'] = 25
print(alien_0)

print('***************************************')
print("6.2.4 �޸��ֵ��е�ֵ")
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + 


