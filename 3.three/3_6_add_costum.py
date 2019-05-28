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
