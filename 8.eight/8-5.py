# -*- coding: gb18030 -*-

def describe_city(city, country = 'England'):
    print(city.title() + " is in " + country.title() + "。")

describe_city(city = 'london')
describe_city(city = 'Birmingham')
describe_city(city = 'new york', country = 'America')
