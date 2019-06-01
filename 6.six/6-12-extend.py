# -*- coding:gb18030 -*-

# 外星人ID测试
# 
# 

# for alien_number in range(1,5,2):
    # new_alien = {'id': alien_number}
    # print(new_alien)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 10}

aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
    # print(alien)

for alien in aliens:
#    print(type(alien))
    for key, value in alien.items():
#        print("alien: " + str(alien))
        print("\t" + key.title() + " is " + str(value))
