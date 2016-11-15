# parking_fines.py

months = 0
ticket = 60

while ticket > 0:
	response = raw_input('Have you paid your ticket? yes/no: ')
	if response == 'yes':
		ticket = 0
	else:
		ticket *= 2	
		print('Okay, your ticket is now ' + str(ticket) + ' dollars')
