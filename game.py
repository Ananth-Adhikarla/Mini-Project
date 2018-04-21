"""
List of Rooms :

Main Entrance = main_room() - id = 0
Left Room = left_room1() - id = 1
Right Room = right_room1() - id = 2

"""



import sys
import os

# turn_on = Main power switched on or off . Game only works if its turned on
turn_on = False
# all the rooms available in the game
room_name = { 0 : "Main Entrance" , 1 : "Left Room 1" , 2 : "Right Room 1" , 3 : "Main Hall" , 4 : "Kitchen" , 5 : "Study Room", 6 : "Secret Room"} 
room_count = { "main" : 0 , "left1" : 0 , "right1" : 0 , "hall" : 0 , "kitchen" : 0 , "study" : 0 , "secret" : 0}
room_index = {  "main" : 0 , "left1" : 1 , "right1" : 2 , "hall" : 3 , "kitchen" : 4 , "study" : 5 , "secret" : 6}
# index of the current room number
current_room_num = 0
# list of items user has collected
inventory = { "letter" : 0, "hammer_head" : 0 , "hammer_stick" : 0 , "axe" : 0 , "backpack" : 0 , "hammer" : 0  , "diamond" : 0  , "photo" : 0}
#chest
chest = 0

def check_light(num):

	global turn_on

	if(turn_on == True):
		if(num == 0):
			print(str.center("You already turned on the main switch.",200))
			return True
		else:
			return True

	else:
		if(num == 0):
			print(str.center("You cannot see anything. Its too dark here",200))
			print(str.center("Find the main switch and turn it on.",200))
			change_room(num)
		else:
			print(str.center("You cannot see anything. Its too dark here",200))
			print(str.center("Find the main switch and turn it on.",200))
			print(str.center("There is no main switch in this room!. ",200))
			change_room(num)

		

def curr_room(num):

	global room_name  

	present_room = room_name[num]
	
	print("****************************************")
	print("Current Room : ", present_room , end = '')
	print("\n")
	print("****************************************")
	
	print("Inventory List :",end = ' ')
	inv_display()

	print("\n")
	
def search_room(room_num):
	global inventory
	global chest

	check = check_light(room_num)
	if(check == True):
		if(room_num == 0):
			if(inventory["backpack"] == 1):
				print(str.center("You already have a backpack",200))
				print(str.center("You are stil in Main room",200))
				change_room(room_num)
			else:
				print(str.center("You find a small backpack",200))
				print(str.center("Do you want to take the backpack?",200))
				inp = input()
				inp1 = inp.split(" ")
				if(inp == 'y' or inp == 'Y' or inp == "yes" or "take" in inp1):
					inv = { "backpack" : 1}
					inventory.update(inv)
					change_room(room_num)

		if(inventory["backpack"] == 1):
			if(room_num == 1):
				print(str.center("You managed to find a letter",200))
				inv = { "letter" : 1 }
				inventory.update(inv)
				print(str.center("Do you wish to open the letter?",200))
				select = input()
				sel = select.split(" ")
				if("yes" in sel or "open" in sel or "read" in sel):
					open_letter(room_num)
					change_room(room_num)

			if(room_num == 2):
				print(str.center("You see a chest and it has a padlock",200))
				print(str.center("Do you wish to break open the chest?",200))
				select = input()
				sel = select.split(" ")
				if("yes" in sel or "open" in sel or "hit" in sel or "break" in sel):
					if(chest == 0):
						open_chest(room_num)
						change_room(room_num)
					else:
						print(str.center("Chest is already opened",200))
						change_room(room_num)
			if(room_num == 3):
					print(str.center("Where do you want to search in the hall? Sofa or Side Drawer?",200))
					inp = input()
					inp = inp.split(" ")
					if( "sofa" in inp or "couch" in inp):
						check_sofa(room_num)
						change_room(room_num)
					elif( "drawer" in inp or "draw" in inp or "side" in inp):
						check_draw(room_num)
						change_room(room_num)
					else:
						print(str.center("Your choice does not exist",200))
						change_room(room_num)

			if(room_num == 4):
				print(str.center("Searching the kitchen!",200))
				search_kitchen(room_num)
				change_room(room_num)

			if(room_num == 5):
				print(str.center("Searching the Study Room!",200))
				search_study(room_num)
				change_room(room_num)

			if(room_num == 6):
				search_secret(room_num)
				change_room(room_num)
		else:
			print(str.center("You need a backpack to collect items. Go find one ! ",200))
			change_room(room_num)
	

def change_room(num):
	
	global inventory

	if(num == -1):
		if(inventory['diamond'] == 0 ):
			print(str.center("You cannot leave without finding the treasure!",200))
			main_room()
		else:
			end_game()

	elif(num == 0):
		main_room()
	elif(num == 1):
		left_room1()
	elif(num == 2):
		right_room1()
	elif(num == 3):
		hall()
	elif(num == 4):
		kitchen()
	elif(num == 5):
		study()
	elif(num == 6):
		secret()

def combine(num):

	global current_room_num
	global inventory

	if(inventory['hammer_head'] == 1 and inventory['hammer_stick'] == 1):
		print(str.center("You combined both the items to create a hammer",200))
		inv = { "hammer_head" : 0 , "hammer_stick" : 0,"hammer" : 1 }
		inventory.update(inv)
		change_room(num)
	else:
		print(str.center("Nothing to combine",200))
		change_room(num)

def open_letter(room_num):

	global inventory
	
	if( inventory['letter'] == 1 ):
		print(str.center("Dear Tomma,",200))
		print(str.center("I was not able to attend your invitational party,",200))
		print(str.center("Hope its all good with you.",200))
		print(str.center("To make up for the miss I have a small precious gift for you",200))
		print(str.center("Take good care of it.",200))

		print(str.center("*********************************************************************",200))

		print(str.center("Me: Oh wow a precious gift. I should try to find it",200))

		change_room(room_num)
	else:
		print("You have no letters go find one.")
		change_room(room_num)

def open_photo(room_num):

	global inventory
	
	if( inventory['photo'] == 1 ):
		print(str.center("You see the photo of Tomma,",200))
		print(str.center("You turn the photo around and find a message,",200))
		print(str.center("it reads,",200))
		print(str.center("Before Mt.Everest was dicovered, what was the highest mountain in the world?,",200))
		print(str.center("*********************************************************************",200))

		change_room(room_num)
	else:
		print("You have no letters go find one.")
		change_room(room_num)
		
def open_chest(room_num):

	global inventory
	global chest

	if( inventory['hammer'] == 1 ):
		print(str.center("You smash the padlock and break it open,",200))
		print(str.center("and you slowly open the chest,",200))
		print(str.center("and find a axe,",200))
		print(str.center("*********************************************************************",200))
		inv = { "axe" : 1 }
		inventory.update(inv)
		chest = 1
		change_room(room_num)

	elif ( inventory['hammer_head'] == 1 ):
		print(str.center("You only have hammer head, find the hammer stick and combine it.",200))
		change_room(room_num)

	elif ( inventory['hammer_stick'] == 1 ):
		print(str.center("You only have hammer stick go find the hammer head and combine it.",200))
		change_room(room_num)

	elif ( inventory['hammer_stick'] == 1 and inventory['hammer_head'] == 1 ):
		print(str.center("You the required parts to combine it.",200))
		change_room(room_num)

	elif ( inventory['hammer_head'] == 0 and inventory['hammer_stick'] == 0 ):
		print(str.center("You dont have any hammer.",200))
		change_room(room_num)

def check_sofa(room_num):

	global inventory

	if( inventory['hammer_head'] == 0 ):
		print(str.center("You check under the sofa and find a hammer head find the stick and combine it",200))
		inv = {'hammer_head' : 1 }
		inventory.update(inv)
		return
	else:
		print(str.center("Nothing else to find here",200))
		return

def check_draw(room_num):
	
	global inventory

	print(str.center("You open the drawer.",200))
	print(str.center("and you find a photo",200))
	inv = {'photo' : 1 }
	inventory.update(inv)
	open_photo(room_num)
	
	return

		
def search_kitchen(room_num):

	global inventory

	if(inventory['hammer_stick'] == 0):
		print(str.center("You search and find a hammer stick, find the head and combine it",200))
		inv = {"hammer_stick" : 1 }
		inventory.update(inv)
		return

	else:
		print(str.center("Nothing else to find here",200))
		return


def search_study(room_num):

	global inventory

	if(inventory['axe'] == 1):
		print(str.center("You search and see a small hole behind the shelf",200))
		print(str.center("You push the shelf to find the hole covered with hard wood pinned with nails",200))
		print(str.center("Do you want to break the wood with your axe?",200))
		print("\n\n")
		choice = input()
		choice = choice.split(" ")
		if("break" in choice or "open" in choice or "yes" in choice or "y" in choice):
			print(str.center("You break the wood with you axe and enter into the secret room",200))
			change_room(6)
		
	else:
		print(str.center("You search and see a small hole behind the shelf",200))
		print(str.center("You push the shelf to find the hole covered with hard wood pinned with nails",200))
		print(str.center("You need a axe to break it open",200))
		change_room(room_num)

def search_secret(room_num):

	global inventory

	
	if(room_count["secret"] == 0 ):
		
		print(str.center("You search the room and see a small box in the corner amongst a lot of junk items",200))
		print(str.center("You take the box and try to open it but it does not open",200))
		print(str.center("you turn the box and find that it requires a secret code",200))
		print(str.center("what do you want to do now?",200))
		user_input = input()
	else:
		print(str.center("you turn the box and find that it requires a secret code",200))
		print(str.center("what do you want to do now?",200))
		user_input = input()
	
	room_count["secret"] =	 1

	user_input = user_input.split(" ")

	if("back" in user_input):
		change_room(5)

	elif("quit" in user_input or "exit" in user_input):
		sys.exit()
	
	elif("up" in user_input or "forward" in user_input):
		print(str.center("You cannot go forward anymore!",200))
		change_room(current_room_num)

	elif("left" in user_input):
		print(str.center("You cannot go left! You are blocked by a wall!",200))
		change_room(current_room_num)

	elif("right" in user_input):
		print(str.center("You cannot go right! You are blocked by a wall!",200))
		change_room(current_room_num)		


	elif("photo" in user_input):
		open_photo(room_num)

	elif("open" in user_input or "secret" in user_input or "box" in user_input):
		open_box(room_num)
		
	else:
		search_secret(current_room_num)

def open_box(num):

	print(str.center("Enter the secret code",200))
	
	choice = input()

	choice = choice.split(" ")

	if("everest" in choice):
		print(str.center("Your code works!",200))
		print(str.center("You open the box and find the secret treasue!",200))
		print(str.center("You find a big diamond!",200))
		inv = { "diamond" : 1 }
		inventory.update(inv)
		change_room(num)
	elif("photo" in choice):
		open_photo()
		open_box()	
	else:
		print(str.center("You entered the wrong code",200))
		change_room(num)



def inv_display():

	for key in inventory:
		if(inventory[key] == 1):
			print(key,":",inventory[key], end = '  ',sep = '  ')
		
	print("\n")	


def main_game():
	
	print("************************************************************************************************************************************************************************************************************\n\n")
		

	print(str.center("Welcome to Ghost House",200))
	print(str.center("Goal is to find a way to escape \n",200))
	
	
	print("************************************************************************************************************************************************************************************************************\n\n")
	
	print(str.center("You see a old house \n",200))
	
	print(str.center("You feel a little adventurous today and decide to enter",200))
	print(str.center(" *THUD* the door closes and you try to open the door but its jammed \n",200))
	print(str.center("There is a room to your left and right and a hall in front",200))
	print(str.center("There is a tiny hint of street light passing through from the windows",200))
	flag = True
	
	while(flag):
		
		print(str.center("What do you want to do now?",200))
		
		main_room()

		
#main room 
def main_room():
	
	global turn_on
	global current_room_num 
	global entry_num
	global room_index

	current_room_num = 0

	curr_room(current_room_num)

	index = 0

	print(str.center("You are currently in main entrance",200))
	print("\n\n")

	choice = input()
		
	power = choice.split(" ")

	if("light" in power or "switch" in power or "mains" in power or "main" in power or "turn" in power or "on" in power):
		turn_on = True
		print(str.center("You successfully managed to turn on the main switch. ",200))
		change_room(current_room_num)		
		
	elif("left" in power ):
		index = room_index["left1"]
		change_room(index)
	
	elif("right" in power):
		index = room_index["right1"]
		change_room(index)

	elif("hall" in power or "up" in power ):
		index = room_index["hall"]
		change_room(index)

	elif( "back" in power):
		index = -1
		change_room(index)
		
	elif( "quit" in power or "exit" in power ):
		sys.exit()
		
	elif("search" in power or "look" in power or "find" in power):
		search_room(current_room_num)
		
	elif( "combine" in power):
		combine(current_room_num)
	elif( "photo" in user_input):
		open_photo(current_room_num)
			
	else:
		print(str.center("Your choice does not exist! Try Again? ",200))
		change_room(current_room_num)
		

# Left Room 1
def left_room1():


	global turn_on
	global current_room_num
	global room_count
	global inventory
	current_room_num = 1

	curr_room(current_room_num)
	if(room_count["left1"] == 0 ):
		os.system('clear')
		curr_room(current_room_num)
		print(str.center("*Struggles* After a hard push you managed to open the rusty door!",200))
		print(str.center("What do you want to do here?",200))
		user_input = input()
		

	else:
		print(str.center("What do you want to do here?",200))
		user_input = input()
		
	user_input = user_input.split(" ")

	room_count["left1"] = 1
	
	if("back" in user_input):
		print(str.center("You have come back to the main entrance.",200))
		print(str.center("Where do you wish to go? Left Room or Right Room or To the hall?",200))
		change_room(0)
	elif("quit" in user_input or "exit" in user_input):
		sys.exit()	
	
	check = check_light(current_room_num)
	
	if(check == True):

		if("up" in user_input or "forward" in user_input):
			print(str.center("You cannot go forward anymore!",200))
			change_room(current_room_num)
		elif("left" in user_input):
			print(str.center("You cannot go left! You are blocked by a wall!",200))
			change_room(current_room_num)
		elif("right" in user_input):
			print(str.center("You cannot go right! You are blocked by a wall!",200))
			change_room(current_room_num)
					
		elif("search" in user_input or "look" in user_input or "find" in user_input):
			if(inventory["letter"] == 1 and inventory["torch"] == 1):
				print(str.center("Nothing to find here",200))
			else:
				search_room(current_room_num)

		elif( "combine" in user_input):
			combine(current_room_num)	
	
		elif( "photo" in user_input):
			open_photo(current_room_num)		
		
		elif( "quit" in user_input or "exit" in user_input ):
			sys.exit()

		else:
			change_room(current_room_num)

def right_room1():
	
	global current_room_num
	global inventory
	current_room_num = 2

	curr_room(current_room_num)

	if(room_count["right1"] == 0 ):
		os.system('clear')
		print(str.center("You push the door it opens easily!",200))
		print(str.center("What do you want to do here?",200))
		user_input = input()

	else:
		print(str.center("What do you want to do here?",200))
		user_input = input()
	
	room_count["right1"] =	 1

	user_input = user_input.split(" ")

	if("back" in user_input):
		change_room(0)
	elif("quit" in user_input or "exit" in user_input):
		sys.exit()

	check = check_light(current_room_num)		
	
	if(check == True):

		if("up" in user_input or "forward" in user_input):
			print(str.center("You cannot go forward anymore!",200))
			change_room(current_room_num)

		elif("left" in user_input):
			print(str.center("You cannot go left! You are blocked by a wall!",200))
			change_room(current_room_num)
		elif("right" in user_input):
			print(str.center("You cannot go right! You are blocked by a wall!",200))
			change_room(current_room_num)
				
		elif("search" in user_input or "look" in user_input or "find" in user_input):
			if(inventory["hammer"] == 1 and chest == 1):
				print(str.center("Nothing to Find here",200))
				change_room(current_room_num)

			elif(inventory["hammer"] == 1 and chest == 0):
				search_room(current_room_num)	
				change_room(current_room_num)
			else:
				print(str.center("Find a hammer to open the chest",200))
				change_room(current_room_num)

		elif( "combine" in user_input):
			combine(current_room_num)
		elif( "photo" in user_input):
			open_photo(current_room_num)

		elif( "quit" in user_input or "exit" in user_input ):
			sys.exit()

		else:
			change_room(current_room_num)
	
def hall():
	
	global current_room_num
	current_room_num = 3

	curr_room(current_room_num)
	
	
	if(room_count["hall"] == 0 ):
		os.system('clear')
		print(str.center("You walk in to to main hall!",200))
		print(str.center("Its filled with dust and torn furniture",200))
		print(str.center("There is a kitchen in front , A room to the left and Main Entrance in the back",200))
		print(str.center("What do you want to do here?",200))	
		user_input = input()

	else:
		print(str.center("What do you want to do here?",200))
		user_input = input()

	
	room_count["hall"] = 1	

	user_input = user_input.split(" ")

	if("back" in user_input):
		print(str.center("You have come back to the main entrance.",200))
		print(str.center("Where do you wish to go? Left Room or Right Room or To the hall?",200))
		change_room(0)

	elif("quit" in user_input or "exit" in user_input):
		sys.exit()

	check = check_light(current_room_num)

	if(check == True):
				
		if("search" in user_input or "look" in user_input or "find" in user_input):
			search_room(current_room_num)

		elif("up" in user_input or "forward" in user_input or "kitchen" in user_input):
			change_room(4)

		elif("left" in user_input):
			change_room(5)

		elif("right" in user_input):
			print(str.center("You cannot go right! You are blocked by a wall!",200))
			change_room(current_room_num)
	
		elif( "combine" in user_input):
			combine(current_room_num)

		elif( "photo" in user_input):
			open_photo(current_room_num)

		else:
			change_room(current_room_num)



def kitchen():
	
	global current_room_num
	global inventory
	current_room_num = 4
	curr_room(current_room_num)

	if(room_count["kitchen"] == 0 ):
		os.system('clear')
		print(str.center("You enter into the kitchen",200))
		print(str.center("What do you want to do here",200))
		user_input = input()

	else:
		print(str.center("What do you want to do here?",200))
		user_input = input()
	
	room_count["kitchen"] =	 1

	user_input = user_input.split(" ")

	if("back" in user_input):
		change_room(3)
	elif("quit" in user_input or "exit" in user_input):
		sys.exit()

	check = check_light(current_room_num)		

	if(check == True):
				
		if("up" in user_input or "forward" in user_input):
			print(str.center("You cannot go forward anymore!",200))
			change_room(current_room_num)

		elif("left" in user_input):
			print(str.center("You cannot go left! You are blocked by a wall!",200))
			change_room(current_room_num)

		elif("right" in user_input):
			print(str.center("You cannot go right! You are blocked by a wall!",200))
			change_room(current_room_num)		

		
		elif("search" in user_input or "look" in user_input or "find" in user_input):
			search_room(current_room_num)

		elif( "combine" in user_input):
			combine(current_room_num)
		
		elif( "photo" in user_input):
			open_photo(current_room_num)
		
		else:
			change_room(current_room_num)



def study():
	
	global current_room_num
	global inventory
	current_room_num = 5
	curr_room(current_room_num)

	if(room_count["study"] == 0 ):
		os.system('clear')
		print(str.center("You enter into the Study Room",200))
		print(str.center("What do you want to do here",200))
		user_input = input()

	else:
		print(str.center("What do you want to do here?",200))
		user_input = input()
	
	room_count["study"] =	 1

	user_input = user_input.split(" ")

	if("back" in user_input):
		change_room(3)

	elif("quit" in user_input or "exit" in user_input):
		sys.exit()

	check = check_light(current_room_num)		

	if(check == True):
				
		if("up" in user_input or "forward" in user_input):
			print(str.center("You cannot go forward anymore!",200))
			change_room(current_room_num)

		elif("left" in user_input):
			print(str.center("You cannot go left! You are blocked by a wall!",200))
			change_room(current_room_num)

		elif("right" in user_input):
			print(str.center("You cannot go right! You are blocked by a wall!",200))
			change_room(current_room_num)		
		
		elif("search" in user_input or "look" in user_input or "find" in user_input):
			search_room(current_room_num)

		elif( "combine" in user_input):
			combine(current_room_num)

		elif( "photo" in user_input):
			open_photo(current_room_num)		
		else:
			change_room(current_room_num)


def secret():

	current_room_num = 6

	curr_room(current_room_num)

	print(str.center("You enter into the secret room",200))
	print(str.center("What do you want to do now?",200))
	
	user_input = input()
	user_input = user_input.split(" ")

	if("back" in user_input):
		change_room(5)
	elif("quit" in user_input or "exit" in user_input):
		sys.exit()
	
	elif("up" in user_input or "forward" in user_input):
		print(str.center("You cannot go forward anymore!",200))
		change_room(current_room_num)

	elif("left" in user_input):
		print(str.center("You cannot go left! You are blocked by a wall!",200))
		change_room(current_room_num)

	elif("right" in user_input):
		print(str.center("You cannot go right! You are blocked by a wall!",200))
		change_room(current_room_num)		

		
	elif("search" in user_input or "look" in user_input or "find" in user_input):
		search_room(current_room_num)

	elif( "combine" in user_input):
		combine(current_room_num)

	elif( "photo" in user_input):
		open_photo(current_room_num)
		
	else:
		change_room(current_room_num)
	
	
def end_game():

	os.system('clear')

	print("************************************************************************************************************************************************************************************************************\n\n")
		

	print(str.center("Credits",200))
	
	
	print("************************************************************************************************************************************************************************************************************\n\n")
	

	
	
	print(str.center("Thank you for playing! Hope you had fun",200))
	print(str.center("Created by: Ananth",200))
	print(str.center("End of game",200))
	

	sys.exit()	
	
main_game()
