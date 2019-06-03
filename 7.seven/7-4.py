# -*- coding: gb18030 -*-

# print("7-4")

prompt = "Please add ingredients: "
prompt += "\n(Enter 'quit' to the end)"



while True:
    message = input(prompt)
    if  message != 'quit': 
        print("We will add " + message)
    else:
        break
