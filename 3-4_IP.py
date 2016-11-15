fave = 14
x = 1
while x == 1:
	print('')
        print('Pick a number from 1 to 100. Type "quit" to end')
        end = raw_input()
        user = int(end)

        if user == fave:
                print('Hooray, you won! Good choice.')
                x = 0
        if user < fave and x == 1:
                print('I don\'t like that number! - try another!')
        if user > fave and x == 1:
                print('I don\'t like that number! - try another!')
        if user % fave == 0 and x == 1:
                print('Here\'s a hint! Your number was a multiplier of mines')
        if float(fave) / user == fave / user and x == 1:
                print('Here\'s a hint! Your number was a divisor of mines')
        if end == 'quit':
                print('Thanks for playing!')
                x = 0

