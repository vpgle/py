# -*- coding: gb18030 -*-

prompt = 'If you could visit one place in the world, where would you go?'
print("enter 'q' to any time to quit!")

like_visit_place = {}
polling_active = True
while polling_active:
    name = input("What's your name? ")
    if name == 'q':
        break

    place = input(prompt)
    if place == 'q':
        break
    
    like_visit_place[name] = place
    
for name, place in like_visit_place.items():
    print(name + " like " + place + "!")

