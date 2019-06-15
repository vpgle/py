# -*- coding: gb18030 -*-

def make_album(singer_name, album_name, num=99):
    album = {}
    album['singer_name'] = singer_name
    album['album_name'] = album_name
    album['number'] = num
    return album

middleware = make_album('lala', 'vwv')
print(middleware)

print(make_album('vivian', 'bilibili'))

print(make_album('shijian', 'sjife'))

middleware = make_album('temp', 'fangke', 66)
# 因为这是字典，所以可以直接打印数字无需转换成字符串
print(middleware)
