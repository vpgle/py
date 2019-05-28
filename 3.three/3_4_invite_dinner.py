# coding=gb18030

invite = ['阿尔伯特·爱因斯坦',
          '富兰克林·罗斯福',
          '圣母·玛丽亚',
          '牛逼哄哄·judge']
print("我要邀请以下人与我共进晚餐：" + invite[0] + '， '
                               + invite[1] + '， '
                               + invite[2] + '， '
                               + invite[3])

wayout = '牛逼哄哄·judge'
invite.remove(wayout)

invite.append('屌·Mr')

print(wayout.title() + "因故无法参加晚宴")

print("我要邀请以下人与我共进晚餐：" + invite[0] + '， '
                               + invite[1] + '， '
                               + invite[2] + '， '
                               + invite[3])
