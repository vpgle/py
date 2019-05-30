# -*- coding: gb18030 -*-

rivers = {
    'nile': 'egypt',
    'Mississippi': 'america',
    'changjiang': 'china',
    }

print(rivers)

for river, country in rivers.items():
    print("The " + river.title() + ' River is located in ' + country.title())
