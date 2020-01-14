# 产生一个1~100的随机整数
# 让使用者重复输入数字去猜
# 猜对的话  印出“终于猜对了！”
# 猜错的话  告诉他比答案大/小
# 显示这是选手猜的第几次
import random # 从图书馆里取书 即从package里面取module
r = random.randint(1,100) # randint=random+int=随机整数
count = 0
while True:
	count += 1 # (count += 1) = (count = count + 1)
	number = input('请输入数字: ')
	number = int(number)
	if r == number:
		print('终于猜对啦了！')
		print('这是你猜的第', count, '次')
		break
	elif r > number:
		print('比答案小')
	else:
		print('比答案大')
	print('这是你猜的第', count, '次')