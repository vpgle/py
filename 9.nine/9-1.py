# -*- coding: gb18030 -*-

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name.title() + ".")
        print("Cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("Opening!!!")

restaurant = Restaurant("糟粕醋", "小吃")


print(restaurant.restaurant_name + " " + restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
