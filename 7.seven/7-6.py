# -*- coding: gb18030 -*-

prompt = "���������䣺"
active = True

while active:
    message = input(prompt)
    if message == 'quit':
        print("��ӭ�´ι���")
        break
    if int(message) < 3 and int(message) > 0:
        print("��������ѹۿ���Ӱ")
    elif int(message) < 12 and int(message) >= 3:
        print("Ʊ��$10")
    elif int(message) > 12:
        print("Ʊ��$15")
    elif int(message) == 0:
        active = False
