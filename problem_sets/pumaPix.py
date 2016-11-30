#create empty list
TVshows = []
#create variables
x = 1
y = 2
#create while loop with condition
while x != y:
	print 'Enter your favorite TV shows (type "done" when you\'re done):'
	show = raw_input()
	if show == 'done':
		y = 1
	else:
#add shows to the list
		TVshows.append(show) 
print 'Okay, here\'s what you entered:'
#print list
print TVshows
print 'We\'ve added a couple of important ones.'
#add ESSENTIAL tv shows to list
TVshows.append('Breaking Bad')
TVshows.append('The Wire')
#sorts show in alphabetical order
TVshows.sort()
#make variable to number the list
count = 1

for show in TVshows:
	print str(count) + '.', show
	count += 1

