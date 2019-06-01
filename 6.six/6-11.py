# -*- coding:gb18030 -*-

cities = {
    'beijing' : {
        'country': 'china',
        'population': '10billion',
        'fact': 'Forbidden City',
        },
    
    'newyork' : {
        'country': 'USA',
        'population': '300million',
        'fact': 'Statue of Liberty',
        },
    
    'paris' : {
        'country': 'french',
        'population': '40million',
        'fact': 'Notre Dame de Paris',
        },
        
        
    }

# for city, user_info in cities.items():
    # print(city + " is " + str(user_info))

for city, user_info in cities.items():
    print("city is " + city)
    print(type(user_info))           #  user_info 是字典类型
    for key, value in user_info.items():
        print(type(value))
        print("\t" + key + " is " + str(value))
