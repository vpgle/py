# -*- coding: gb18030 -*-

print("input 用法")

name = input("Please enter your name: ")
print("Hello, " + name + "!")

print("加长版提示语")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")
