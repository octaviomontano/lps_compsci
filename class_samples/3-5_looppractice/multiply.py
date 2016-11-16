print 'For what number would you like multiples?'
number = float(raw_input())
print 'What would you like your ceiling to be?'
ceiling = int(raw_input())

count = 0
multiple = 0
while multiple < ceiling:
	math = float(count * number)
	print(str(count) + ' times ' + str(number) + ' equals ' + str(math))
	multiple = count * number
	count += 1
print'There are', count ,'integer multiples of', number,'that are less than', str(ceiling) + '. Have a nice day!'

