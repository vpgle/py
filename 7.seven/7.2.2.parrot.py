# -*- coding: gb18030 -*-
'''

'''
print("7.2.2 ���û�ѡ���ʱ�˳�")
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':              #  �ж��ǲ���quit���ǾͲ���ӡ
        print(message)   # ��������ʾ��Ϣǰ�����򵥵ļ�飬������Ϣ����
                          # �˳�ֵʱ�Ŵ�ӡ
    
    
