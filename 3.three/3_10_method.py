# coding=gb18030

states = ['alabama' ,
		  'tennessee' ,
		  'delaware' ,
		  'florida' ,
		  'georgia' ,
		  'pennslyvania' ,
		  'south dakota' ,
		  'idaho' ,
		  'vermont' ,
		  'kansas' ,
		  'louisiana' ,
		  'maine' ,
		  'nebraska' ,
		  'california' ,
		  'ohio' ,
		  'wyoming' ]
print(states)

# ~ print(states[0])
# ~ print(states[1])
# ~ print(states[2])
# ~ print(states[3])
# ~ print(states[4])
# ~ print(states[5])
# ~ print(states[6])
# ~ print(states[7])
# ~ print(states[8])
# ~ print(states[9])
# ~ print(states[10])
# ~ print(states[11])
# ~ print(states[12])
# ~ print(states[13])
# ~ print(states[14])

print("==========================�ǲ��Ƿָ��߶�������������������������������������")

print("һ�����б������Ԫ�صķ���append,insert")
states.append('Utah'.lower())
print(states[-1])

print(states[1])
states.insert(1, 'Oregon'.lower())
print(states[1])

print("-----------------------------�ָ���-----------------------------------")
print("�����޸��б���Ԫ��ֵ")
print(states[10])
states[10] = 'Colorado'
print(states[10])

print("+++++++++++++++++++++++++++++++||++++++++++++++++++++++++++++++++++++")
print("����������4��ɾ��Ԫ�صķ���")
print("1.��������ɾ��Ԫ�أ� del states[-2]")
print("ɾ��ǰstates[-2]ֵ��" + states[-2])
del states[-2]
print("ɾ����states[-2]ֵ��" + states[-2])

print("2.����Ԫ��ֵɾ��Ԫ�أ�remove('ohio')")
print(states)
states.remove('ohio')
print(states)

print("3.��pop()ɾ��ĩβ��Ԫ��")
print(states.pop())
print(states)

print("4.��pop(-5)ָ������ɾ��ֵ")
print("����Ϊ-5��Ԫ��ֵ�� " + states[-5])
print(states.pop(-5))
print(states)


print("******************************!!*************************************")
print("�ġ�2�����򷽷�")
print("��.�������޸��б�����sort(),ԭ�б�˳��ı�")
print("ԭ�б�" )
print(states)
print("����ĸ�����������")
states.sort()
print(states)
print("����ĸ��������������")
states.sort(reverse=True)
print(states)

states = ['alabama' ,
		  'tennessee' ,
		  'delaware' ,
		  'florida' ,
		  'georgia' ,
		  'pennslyvania' ,
		  'south dakota' ,
		  'idaho' ,
		  'vermont' ,
		  'kansas' ,
		  'louisiana' ,
		  'maine' ,
		  'nebraska' ,
		  'california' ,
		  'ohio' ,
		  'wyoming' ]
		  
print("��.��ʱ���޸��б�����sorted(),ԭ�б�˳�򲻱�")
print("ԭ�б�" )
print(states)
print("����ĸ��ʱ�������")
print(sorted(states))
print("�����ٿ���ԭ�б�˳��" )
print(states)
print()
print()
print("����ĸ   ����    ��ʱ������")
print(sorted(states, reverse=True))
print("�����ٿ���ԭ�б�˳��" )
print(states)
print()

print("13.05.201913.05.201913.05.201913.05.201913.05.201913.05.201913.05.2019")
print("                                                             ")

print("�������򣬲��ǰ���ĸ���򣬶��ǰ���Ԫ��˳����")
print("reverse()")
print("����ǰ��")
print(states)
states.reverse()
print("�����")
print(states)

