import random

def ran_num(x,y):

	flag = True	
	
	while(flag):
		r = random.randint(x,y)
		
		print("Your random number is :", r)
		
		print("\nDo you wish to continue? Press Y or N")
	
		status = input()
	
		if( status == 'y' or status == 'Y'):
			flag = True
		else:
			flag = False


ran_num(1,6)
