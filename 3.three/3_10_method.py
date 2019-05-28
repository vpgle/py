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

print("==========================是不是分割线都长这样、、、、、、、、、、、、、、、")

print("一、在列表中添加元素的方法append,insert")
states.append('Utah'.lower())
print(states[-1])

print(states[1])
states.insert(1, 'Oregon'.lower())
print(states[1])

print("-----------------------------分割线-----------------------------------")
print("二、修改列表中元素值")
print(states[10])
states[10] = 'Colorado'
print(states[10])

print("+++++++++++++++++++++++++++++++||++++++++++++++++++++++++++++++++++++")
print("三、下面是4中删除元素的方法")
print("1.根据索引删除元素， del states[-2]")
print("删除前states[-2]值是" + states[-2])
del states[-2]
print("删除后states[-2]值是" + states[-2])

print("2.根据元素值删除元素，remove('ohio')")
print(states)
states.remove('ohio')
print(states)

print("3.用pop()删除末尾的元素")
print(states.pop())
print(states)

print("4.用pop(-5)指定索引删除值")
print("索引为-5的元素值是 " + states[-5])
print(states.pop(-5))
print(states)


print("******************************!!*************************************")
print("四、2种排序方法")
print("①.永久性修改列表排序sort(),原列表顺序改变")
print("原列表：" )
print(states)
print("按字母永久性排序后")
states.sort()
print(states)
print("按字母倒序永久性排序")
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
		  
print("②.临时性修改列表排序sorted(),原列表顺序不变")
print("原列表：" )
print(states)
print("按字母临时性排序后")
print(sorted(states))
print("我们再看下原列表顺序：" )
print(states)
print()
print()
print("按字母   倒序    临时性排序")
print(sorted(states, reverse=True))
print("我们再看下原列表顺序：" )
print(states)
print()

print("13.05.201913.05.201913.05.201913.05.201913.05.201913.05.201913.05.2019")
print("                                                             ")

print("倒序排序，不是按字母排序，而是按照元素顺序倒叙")
print("reverse()")
print("倒叙前：")
print(states)
states.reverse()
print("倒叙后：")
print(states)

