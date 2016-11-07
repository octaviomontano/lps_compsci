print('Enter the amount of purchases, in cents:')
amount = int(raw_input())
if amount > 1000:
	discount = amount * .1
	total = amount - discount
	print('You spent over $10! Your final price is ' + str(total) + ' cents')
