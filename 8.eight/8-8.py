# -*- coding: gb18030 -*-

def make_album(singer_name, album_name, num=99):
    album = {}
    album['singer_name'] = singer_name
    album['album_name'] = album_name
    album['number'] = num
    return album

while True:
    print("(enter 'q' at any time to quit)")
    singer_name = input("�������������")
    if singer_name == 'q':
        break
    
    album_name = input("������ר������")
    if album_name == 'q':
        break
    
    print("ר����� " + str(make_album(singer_name, album_name)))





