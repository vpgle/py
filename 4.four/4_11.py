# -*- coding: GB18030 -*-


pizzas = ['����Ģ������',          '��԰�߲�����',          '�㹽��������']
          
friend_pizzas = pizzas[:]

pizzas.append('Toma pizza')
friend_pizzas.append('italian pizza')


for pizza in pizzas:
    print("I like " + pizza)


print("I really love pizza!")



print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
    
print("My friend's favorite pizzas are")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
    
