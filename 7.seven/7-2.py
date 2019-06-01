# -*- coding: gb18030 -*-

message = input("请问几位？ ")

if int(message) > 8:
    print("抱歉，现在没有空桌")
else:
    print("有空桌，请跟我来")
