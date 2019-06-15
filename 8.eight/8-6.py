# -*- coding: gb18030 -*-

def city_country(city, country):
    str = '"' + city.title() + ', ' + country.title() + '"'
    return str

stri = city_country("santiage", "chile")
print(stri)

stri = city_country('new york', 'america')
print(stri)

stri = city_country("tokyo", 'japan')
print(stri)
