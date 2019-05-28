# coding=gb18030

places = ['new Zealand',
		  'america',
          'france',
          'china',
          'japan']

print(places)

print(sorted(places))
print(places)

print("使用sorted(places,reverse=True)按与字母顺序相反的顺序打印这个列表，同时不要修改它。")
print(sorted(places,reverse=True))
print(places)

print("====================================================================")
print("使用reverse()修改列表元素的排列顺序。")
print("打印该列表，核实排列顺序确实变了.")
places.reverse()
print(places)

print("使用reverse()再次修改列表元素的排列顺序。")
print("打印该列表，核实已恢复到原来的排列顺序。")
places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)
