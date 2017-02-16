import random
randomLine = ['Baby don\'t hurt me','Once upon a time','A fast potato','To infinity and beyond','To who it concerns','Oh mathematics']

print 'Welcome to the Haiku generator!'
print 'Would you like to write your haiku from scratch or get a randomized first line?'
print '(1) I\'ll write it from scratch'
print '(2) Start me with a random line'
choice = input()

if choice == 1:
	print 'Provide the first line of your haiku:'
	firstL = raw_input()
	print 'Provide the second line of your haiku:'
	secondL = raw_input()
	print 'Provide the third line of your haiku:'
	thirdL = raw_input()
	print 'What file would you like to write your haiku to?'
	name = raw_input()

if choice == 2:
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

haiku = open(name, 'w')
haiku.write(firstL + '\n')
haiku.write(secondL + '\n')
haiku.write(thirdL + '\n')
haiku.close()
