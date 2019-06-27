# -*- coding: gb18030 -*-

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_user(self):
        print("My name is " + self.first_name.title() 
                      + " " + self.last_name.title())
    
    def greet_user(self):
        print("Nice to meet you, " + self.first_name.title()
                                + " " + self.last_name.title())


me = User("vicence", "Lee")
me.describe_user()
me.greet_user()

you = User("道明", "陈")
you.describe_user()
you.greet_user()

it = User("里", "li")
it.describe_user()
it.greet_user()
