# -*- coding: gb18030 -*-

prompt = "请输入年龄："
active = True

while active:
    message = input(prompt)
    if message == 'quit':
        print("欢迎下次光临")
        break
    if int(message) < 3 and int(message) > 0:
        print("您可以免费观看电影")
    elif int(message) < 12 and int(message) >= 3:
        print("票价$10")
    elif int(message) > 12:
        print("票价$15")
    elif int(message) == 0:
        active = False
