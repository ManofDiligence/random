import random
r = random.randint(1, 100)
count = 0
while True:
	count = count + 1
	num = input('please guess the number:')
	num = int(num)
	if num == r:
		print('the answer is correct!')
		print('this is ur ',count,'time to guess the number.')
		break
	elif num > r:
		print('This number is bigger than the answer')
	elif num < r:
		print('smaller than the ans')
	print('this is ur ',count,'time to guess the number.')
