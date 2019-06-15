# -*- coding: gb18030 -*-

def make_album(singer_name, album_name, num=99):
    album = {}
    album['singer_name'] = singer_name
    album['album_name'] = album_name
    album['number'] = num
    return album

while True:
    print("(enter 'q' at any time to quit)")
    singer_name = input("请输入歌手名：")
    if singer_name == 'q':
        break
    
    album_name = input("请输入专辑名：")
    if album_name == 'q':
        break
    
    print("专辑简介 " + str(make_album(singer_name, album_name)))





