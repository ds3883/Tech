import random

#system generate random 4 number in list
def sys():
	ans = []
	
	while len(ans)<4:
		n = random.randrange(0,10)
		if not n in ans:
			ans.append(n)

	#print('--Debug System Generate Answer--')
	#print(ans)
	return ans
	
#manual input random 4 number in list check
def input_check():
	for n in guess: 
		#check all input number are within the number scope (0~9)
		if n>9:
			return False
		#check for duplicat number & length limitation (4)
		elif len(set(guess)) != 4:
			return False
	return True
				
#setting the answer value from sys() function
answer = sys()
game_on = True

print('** Welcome to 1A2B game')
print('** Please enter 4 numbers from 0 ~ 9 and separate by space')
print('** For example: 1 2 3 4')
	
while game_on:
	user_input = input('** Enter your 4 numbers here: ')
	
	value_check = True
	while value_check: 
		try:
			guess = list(map(int, user_input.split(' ')))
			value_check = False
		#exception error handle for VauleError
		except ValueError:
			print('\n** Please enter 4 numbers from 0 ~ 9')
			print('** Please try again')
			user_input = input('** Enter your 4 numbers here: ')
	
	a, b = 0, 0
	
	if input_check() == True: 
		for n in guess: 
			if n in answer: 
				if guess.index(n) == answer.index(n):
					a += 1 
				else: 
					b += 1

		#print('-- Debug answer --')
		#print(answer)
		print('\n** Your guess is: {}'.format(user_input))
		print('** Your guess result is {}A{}B\n'.format(a,b))
	
	else: 
		print('\n** Please enter 4 numbers from 0 ~ 9 and separate by space')
		print('** For example: 1 2 3 4')
		print('** Numbers cannot repeat')
		print('** Please try again!\n')
	
	if a == 4: 
		print('** Good Job! You got it!')
		game_on = False
	else: 
		print('** Keep trying')