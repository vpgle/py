# -*- coding: gb18030 -*-
# 6.2.4 �޸��ֵ��е�ֵ
alien_0 = {
    'x_position': 0,
    'y_position': 25,
    'speed': 'medium',
    }
print("Original x-position: " + str(alien_0['x_position']))

# �����ƶ�������
# �������˵�ǰ�ٶȾ��������ƶ���Զ
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # ��������˵��ٶ�һ���ܿ�
    x_increment = 3
    
# ��λ�õ�����λ�ü�������
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))    


print("--------------------------------------////////////////")

print('6.2.5 ɾ����ֵ��')
print(alien_0)
del alien_0['x_position']
print(alien_0)
del alien_0['y_position']
print(alien_0)
del alien_0['speed']
print(alien_0)
