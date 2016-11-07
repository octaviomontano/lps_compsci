print('How many miles do you live from Richmond State')
miles = int(raw_input())
print('What\'s your GPA')
gpa = float(raw_input())

if miles <= 30:
        if gpa >= 2.0:
                print('Congratulations, you\'ve been admitted!')
	else:
		print('Sorry, you\'re not qualified')
		tip = 2.0 - gpa
		print('You\'ll need a GPA that is ' + str(tip) + ' higher than your current GPA.')
if miles > 30:
        if gpa >= 2.5:
                print('What\'s your ACT score?')
                act = int(raw_input())
                if act >= 18:
                        print('Congratulations, you\'ve been admitted!')
		else:
                	print('Sorry, you\'re not qualified')
                	tip = 18 - act
                	print('You\'ll need an ACT score that is ' + str(tip) + ' higher than your current score.')
        else:
		print('Sorry, you\'re not qualified')
                tip = 2.5 - gpa
                print('You\'ll need a GPA that is ' + str(tip) + ' higher than your current GPA.')
