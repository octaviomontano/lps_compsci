# to make the functions of this package available
import random
# creates a random number between 1 and 1000
myNum = random.randint(1, 1000)
point = 100
yrNum = 0

while yrNum != myNum:
	print 'I\'m thinking of a number from 1 to 1000. Enter your guess!'
	yrNum = int(raw_input())
	if yrNum == myNum:
		print 'Horray, you won!'
		print 'Your score was', point
	if yrNum > myNum:
		print 'Nope, too high! Guess again.'
	if yrNum < myNum:
		print 'Nope, too low! Guess again.'
	point -= 1
	if point < 1:
		point = 1
