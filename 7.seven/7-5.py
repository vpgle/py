# -*- coding: gb18030 -*-

prompt = "请输入年龄："

while True:
    message = int(input(prompt))
    if message < 3 and message > 0:
        print("您可以免费观看电影")
    elif message < 12 and message >= 3:
        print("票价$10")
    elif message > 12:
        print("票价$15")
    elif message == 0:
        print("欢迎下次光临")
        break
