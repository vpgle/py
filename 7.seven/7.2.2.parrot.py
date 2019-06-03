# -*- coding: gb18030 -*-
'''

'''
print("7.2.2 让用户选择何时退出")
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':              #  判断是不是quit，是就不打印
        print(message)   # 程序在显示消息前将做简单的检查，仅在消息不是
                          # 退出值时才打印
    
    
