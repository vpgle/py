# -*- coding: gb18030 -*-

responses = {}

# ����һ����־��ָ�������Ƿ����
polling_active = True

while polling_active:
    # ��ʾ���뱻�����ߵ����ֺͻش�
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # ���𰸴洢���ֵ���
    responses[name] = response
    
    # �����Ƿ�����Ҫ�������
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# �����������ʾ���
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
