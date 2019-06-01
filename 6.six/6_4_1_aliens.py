# -*- coding:gb18030 -*-

# ������ID����
# 
# 

# for alien_number in range(1,5,2):
    # new_alien = {'id': alien_number}
    # print(new_alien)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 10}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    


# ����һ�����ڴ洢�����˵Ŀ��б�
aliens = []

# ����30����ɫ������
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# ��ʾǰ���������
for alien in aliens[: 5]:
    print(alien)
print("...")

# ��ʾ�����˶��ٸ�������
print("Total number of aliens: " + str(len(aliens)))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# ��ʾǰ���������
for alien in aliens[0:5]:
    print(alien)
print("...")
    
