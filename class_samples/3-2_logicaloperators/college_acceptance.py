print('How old are you?')
age = int(raw_input())

print('What is our GPA')
GPA = float(raw_input())

if GPA > 3.0 and age > 16:
	print(' Congrats, Welcome to Columbia!')
if GPA <= 3.0 or age <= 16:
	print('Sorry, good luck at Harvard.')
