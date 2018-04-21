class tags:

	UNDERLINE = '\033[4m'
	END = '\033[0m'
	BLUE = '\033[94m'

def mad_libs(person, place, adjective1, adjective2, adjective3, noun, plural_noun, plural_noun2, plural_noun3, plural_noun4, action_verb, action_verb2, action_verb3 ):

	per = tags.UNDERLINE + tags.BLUE + person + tags.END
	pal = tags.UNDERLINE + tags.BLUE + place + tags.END
	ad1 = tags.UNDERLINE + tags.BLUE + adjective1 + tags.END
	ad2 = tags.UNDERLINE + tags.BLUE + adjective2 + tags.END
	ad3 = tags.UNDERLINE + tags.BLUE + adjective3 + tags.END
	nou = tags.UNDERLINE + tags.BLUE + noun + tags.END
	plu1 = tags.UNDERLINE + tags.BLUE + plural_noun + tags.END
	plu2 = tags.UNDERLINE + tags.BLUE + plural_noun2 + tags.END
	plu3 = tags.UNDERLINE + tags.BLUE + plural_noun3 + tags.END
	plu4 = tags.UNDERLINE + tags.BLUE + plural_noun4 + tags.END
	av1 = tags.UNDERLINE +  tags.BLUE + action_verb + tags.END
	av2 = tags.UNDERLINE +  tags.BLUE + action_verb2 + tags.END
	av3 = tags.UNDERLINE + tags.BLUE + action_verb3 + tags.END
	

	print("The story is : \n\n")
	print("Summer Trip\n\n")
	print("Last Summer, my mom and dad took me and ",per, "on a trip to ", pal)
	print("The weather there is very ",ad1,"!")
	print("Northern ",place," has many ",plu1,", and they make ", ad2 , " " , plu2, " there.")
	print("Many people also go to ",pal," to ",av1," or see the ", plu3, ".")
	print("The people that live there also love to eat ",plu4, " and they are also very proud of their big ", nou , ".")
	print("They also like to ", av2, " in the sun and swim in the ", av3 , "!")
	print("It was really a ", ad3 , " trip!")
	print("\n")



print("Lets make a story from your word choices!\n")

print("Enter a Persons name :\n")

person = input()

print("Enter a Place :\n")

place = input()

print("Enter adjective1 :\n")

adjective1 = input()

print("Enter adjective2 :\n")

adjective2 = input()

print("Enter adjective3 :\n")

adjective3 = input()

print("Enter a noun :\n")

noun = input()

print("Enter a Plural noun 1 :\n")

plural1 = input()

print("Enter a Plural noun 2 :\n")

plural2 = input()
	
print("Enter a Plural noun 3 :\n")

plural3 =input()
	
print("Enter a Plural noun 4 :\n")

plural4 = input()

print("Enter a action verb 1 :\n")

action1 = input()
	
print("Enter a action verb 2 :\n")
	
action2 = input()	
	
print("Enter a action verb 3 :\n")

action3 = input()

mad_libs(person,place,adjective1,adjective2,adjective3,noun,plural1,plural2,plural3,plural4,action1,action2,action3)

	
