# -*- coding: gb18030 -*-

prompt = "���������䣺"

while True:
    message = int(input(prompt))
    if message < 3 and message > 0:
        print("��������ѹۿ���Ӱ")
    elif message < 12 and message >= 3:
        print("Ʊ��$10")
    elif message > 12:
        print("Ʊ��$15")
    elif message == 0:
        print("��ӭ�´ι���")
        break
