print 'Welcome to the Haiku generator!'
print 'Provide the first line of your haiku:'

firstL = raw_input()

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
