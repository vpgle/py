# coding=gb18030

invite = ['阿尔伯特·爱因斯坦',
          '富兰克林·罗斯福',
          '圣母·玛丽亚',
          '牛逼哄哄·judge']
print("我要邀请以下人与我共进晚餐：" + invite[0] + '， '
                               + invite[1] + '， '
                               + invite[2] + '， '
                               + invite[3])
                               
# 在3-4基础上操作

invite.insert(0, '帝国总裁：落地死先生')
print(invite[0])
invite.insert(2, '上帝之都：秦暴政陛下')      
print(invite[2])                         
invite.append("新人王：迪莉斯汀女士")
print(invite[-1])

print("我要邀请以下人与我共进晚餐：" + invite[0] + '， '
                               + invite[1] + '， '
                               + invite[2] + '， '
                               + invite[3]+ '， '
                               + invite[4] + '， '
                               + invite[5] + '， '
                               + invite[6])
print("我找到了一个更大的餐桌，我要邀请大家吃个便饭")

# 3-7基础上操作

print("十分抱歉，由于新购买的餐桌无法及时送达，只能邀请两位嘉宾。")

del_custom = invite.pop()
print("很抱歉无法与您一起共进晚餐" + ":" + del_custom + "!")
del_custom = invite.pop()
print("很抱歉无法与您一起共进晚餐" + ":" + del_custom + "!")
del_custom = invite.pop()
print("很抱歉无法与您一起共进晚餐" + ":" + del_custom + "!")
del_custom = invite.pop()
print("很抱歉无法与您一起共进晚餐" + ":" + del_custom + "!")
del_custom = invite.pop()
print("很抱歉无法与您一起共进晚餐" + ":" + del_custom + "!")

print("十分高兴能与您共进晚餐" + invite[0])
print("十分高兴能与您共进晚餐" + invite[1])

del invite[0]
del invite[0]
print(invite)
