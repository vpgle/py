# -*- coding: gb18030 -*-

print("confirmed_users")

# ���ȣ�����һ������֤���û��б�
#  ��һ�����ڴ洢����֤�û��Ŀ��б�

unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# ��֤ÿ���û���ֱ��û��δ��֤�û�Ϊֹ
#  ��ÿ��������֤���б��Ƶ�����֤�û��б���
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
# ��ʾ��������֤���û�
print("\nThe following users have seen confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
