import random 

class tags:

	UNDERLINE = '\033[4m'
	END = '\033[0m'

def find_letter(letter , word_split):
	
	for i in word_split:
		if(letter == i):
			return i

def find_index(letter , word_split):

	arr = []
	for pos,i in enumerate(word_split):
		if(letter == i):
			arr.append(pos)
		
	return arr
			
	

def hangman():

	hangman_lists = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
		
	word = random.choice(hangman_lists)

	flag = True

	size_word = len(word)

	blank = '_'
	
	line = tags.UNDERLINE + blank + tags.END
	
	index = [blank]*size_word

	length = 0
	
	arr = []
	
	tries = 10

	print("Guess the word")

	for dash in range(0,size_word):
		print(line, end=' ')
	
	print("\n")

	word_split = list(word)

	while(flag):
		print("Enter a letter \n")
		letter = input()
		print("\n")
		
		if( find_letter(letter,word_split) ):
			length =  find_index(letter,word_split) 
			lsize = len(length)
			if(lsize == 1 ):
				length = int(length[lsize-1])
				index[length] = letter
			else:
				for i in length:
					index[i] = letter
				
		else:
			tries -= 1

		print("length :: ",length)
		print("\n")		
		print(*index,sep=' ')
		print("\n")
		print("Number of tries left : ",tries)
	
		
		if( tries == 0):
			print("\n The correct word was : ", word)
			break
		elif( index == word_split ):
			print("\n End of Game \n")
			break
		else:
			continue
	
hangman()
		

	
