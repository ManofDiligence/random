import random
start = input('please enter the smallest number:')
end = input('please enter the biggest number:')
start = int(start)
end = int(end)

r = random.randint(start, end)
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
	print('this is ur ',count,'times to guess the number.')
