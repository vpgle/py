# coding=gb18030

places = ['new Zealand',
		  'america',
          'france',
          'china',
          'japan']

print(places)

print(sorted(places))
print(places)

print("ʹ��sorted(places,reverse=True)������ĸ˳���෴��˳���ӡ����б�ͬʱ��Ҫ�޸�����")
print(sorted(places,reverse=True))
print(places)

print("====================================================================")
print("ʹ��reverse()�޸��б�Ԫ�ص�����˳��")
print("��ӡ���б���ʵ����˳��ȷʵ����.")
places.reverse()
print(places)

print("ʹ��reverse()�ٴ��޸��б�Ԫ�ص�����˳��")
print("��ӡ���б���ʵ�ѻָ���ԭ��������˳��")
places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)
