# to make the functions of this package available
import random
# creates a random number between 1 and 1000
myNum = random.randint(1, 1000)
point = 100
# ^ variable to track points
# v  define a variable
yrNum = 0
print 'I\'m thinking of a number from 1 to 1000. Enter your guess!'
# v create the loop for the game
while yrNum != myNum:
#ask for guess, and converted to an integar. (I did the whole code and 
#was absolutely sure it would work, but it didn't even though I was certain
#everything was correct and my only problem was that I didn't convert the
#raw_input into an integar vv 
	yrNum = int(raw_input())
#conditions for outputs & checks if guess is correct v
	if yrNum == myNum:
		print 'Horray, you won!'
		print 'Your score was', point
	if yrNum > myNum:
		print 'Nope, too high! Guess again.'
	if yrNum < myNum:
		print 'Nope, too low! Guess again.'
#point subtraction v
	point -= 1
	if point < 1:
		point = 1
