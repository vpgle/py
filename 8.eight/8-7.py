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
# ��Ϊ�����ֵ䣬���Կ���ֱ�Ӵ�ӡ��������ת�����ַ���
print(middleware)
