# coding=gb18030

motorcycles = ['honda',
               'yamaha',
               'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

print("����pop()����ô�����õ��أ������б��е�Ħ�г��ǰ�����ʱ��洢�ģ�")
print("�Ϳ�ʹ�÷���pop()��ӡһ����Ϣ��ָ�����������ǿ�Ħ�г���")

motorcycles.append('suzuki')
print(motorcycles)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

print(motorcycles)

motorcycles.append('suzuki')
print(motorcycles)

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a '+ first_owned.title() + '.')
print(motorcycles)

print("����㲻ȷ����ʹ��del��仹��pop()������������һ���򵥵��жϱ�׼��")
print("�����Ҫ���б���ɾ��һ��Ԫ�أ��Ҳ������κη�ʽʹ��������ʹ��del���")
print("�����Ҫ��ɾ��Ԫ�غ��ܼ���ʹ��������ʹ�÷���pop()")

print("===============================���ǻ����ķָ���=-===============================")
motorcycles = ['honda',
               'yamaha',
               'suzuki',
               'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

print("===============================���ǻ����ķָ���=-===============================")

print("��ĩβ���'ducati'")
motorcycles.append('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")


print("����remove()ֻɾ����һ��ָ����ֵ�����Ҫɾ����ֵ�������б��г��ֶ�Σ�")
print("����Ҫʹ��ѭ�����ж��Ƿ�ɾ��������������ֵ���㽫�ڵ�7��ѧϰ���������")






