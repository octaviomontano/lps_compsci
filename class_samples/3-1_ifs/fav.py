fave = 1300
while True: 
	print('Pick a number from 1 to 1600. Type "quit" to end')
	end = raw_input()
	user = int(end)

	if user == fave:
		print('Hooray, you won! Good choice.') 
		break
	if user < fave:
	        print('Sorry, you lose. :( Try a higher number')
	if user > fave:
	        print('Sorry, you lose. :( Try a lower number')
	if user % fave == 0:
		print('Here\'s a hint! Your number was a multiplier of mines')
	if float(fave) / user == fave / user:
		print('Here\'s a hint! Your number was a divisor of mines')
	if end == 'quit':
		print('Thanks for playing!')
		break   
	continue             
