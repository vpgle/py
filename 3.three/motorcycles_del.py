# coding=gb18030

motorcycles = ['honda',
               'yamaha',
               'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles.insert(0, 'wuling')
print(motorcycles)

print("append('dddd')  ֻ����ӵ�ĩβ")
motorcycles.append('dddd')
print(motorcycles)

print("insert(1, '��������λ��') ���Բ�������λ��")
motorcycles.insert(2, '�����ַ������б�')
print(motorcycles)
