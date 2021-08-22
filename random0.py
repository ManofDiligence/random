import random
r = random.randint(1, 100)
while True:
	num = input('please guess the number:')
	num = int(num)
	if num == r:
		print('the answer is correct!')
		break
	elif num > r:
		print('This number is bigger than the answer')
	elif num < r:
		print('smaller than the ans')
