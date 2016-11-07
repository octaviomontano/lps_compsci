print('Which time zone would you like to convert to California time?')

print('(1) New York')
print('(2) Chicago')
print('(3) London')
print('(4) Tokyo')
print('(5) Dubai')
print('(6) Buenos Aires')
choice = input('Enter the number of the city: ')

if choice == 1:
	city = 'New York'
	timedif = 9
elif choice == 2:
	city = 'Chicago'
	timedif = 10
elif choice == 3:
	city = 'London'
	timedif = 4
elif choice == 4:
        city = 'Tokyo'
        timedif = 8
elif choice == 5:
	city = 'Dubai'
	timedif = 11
elif choice == 6:
	city = 'Buenos Aires'
	timedif = 8
else:
	print('Sorry, that is not one of the choices')

print('What hour is it in ' + city + '?')
Hours = raw_input()
print('What minute is it in ' + city + '?')
Minutes = raw_input()
Time = Hours + ':' + Minutes

CaliforniaHours = (int(Hours) + int(timedif)) % 12
#CaliforniaHours %= 12

CaliforniaTime = str(CaliforniaHours) + ':' + Minutes
print('If the time in ' + city + ' is ' + Time + ', then the time in California is ' + CaliforniaTime)
