# importing the random program to choose a random line from the list I've created
import random
randomLine = ['Baby don\'t hurt me','Once upon a time','A fast potato','To infinity and beyond','To who it concerns','Oh mathematics']

# displays options and prompts choice
print 'Welcome to the Haiku generator!'
print 'Would you like to write your haiku from scratch or get a randomized first line?'
print '(1) I\'ll write it from scratch'
print '(2) Start me with a random line'
choice = input()

# conditional statements that run certain tasks based on user input
if choice == 1:
	# saves lines and text file names to variables
	print 'Provide the first line of your haiku:'
	firstL = raw_input()
	print 'Provide the second line of your haiku:'
	secondL = raw_input()
	print 'Provide the third line of your haiku:'
	thirdL = raw_input()
	print 'What file would you like to write your haiku to?'
	name = raw_input()

if choice == 2:
	# randomly chooses a number that determines the randomly chosen line, then prompts for 2 more lines
	print 'All right, here\'s your first line:'
	num = random.randint(0,6)
	firstL = randomLine[num]
	print firstL + '\n'
	print 'Provide the second line of your haiku:'
        secondL = raw_input()
        print 'Provide the third line of your haiku:'
        thirdL = raw_input()
        print 'What file would you like to write your haiku to?'
        name = raw_input()
print 'Done! To view your haiku, type \'cat\' and the name of your file at the command line.'

# uses variables to create the new file with lines for the haiku
haiku = open(name, 'w')
haiku.write(firstL + '\n')
haiku.write(secondL + '\n')
haiku.write(thirdL + '\n')
haiku.close()
