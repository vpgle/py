# -*- coding: gb18030 -*-

def make_pizza(size, *toppings):
    """����Ҫ����������"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
