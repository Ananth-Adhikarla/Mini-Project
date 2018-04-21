import random

def guess():

	flag = True	

	r = random.randint(1,10)

	count = 5
	
	while(flag):
		
		print("A number is randomly generated between 1-10 and you have to guess the number?\n")
		print("Number of tries left :",count)
		user_guess = int( input() )	
		
		if(user_guess == r):
			print("You have guessed the number correctly!\n")
			print("The number was : ", r)
			print("\n\nEnd of Game!!!!!!!!!!!!!!")
			flag = False
			break;

		elif(user_guess > r):
			print("The number you have guessed is slightly higher\n")

			print("Try again? \n")
		
			count = count-1
	
		elif(user_guess < r):
			print("The number you have guessed is slightly lower\n")
		
			print("Try again? \n")

			count = count-1

		else:
			flag = False

			

status = True

while(status):

	guess()

	print("\n")

	print("Do you wish to play more? Press Y to continue or N to exit !\n")
	
	inp = input()
		
	if(inp == 'y' or inp == 'Y'):
		status = True
	else:	
		status = False
		break

