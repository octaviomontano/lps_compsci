print('How much do the nachos cost?')
cost = int(raw_input())
print('How much money do you have in your pocket?')
greenpaper = int(raw_input())
if greenpaper < cost:
	print('You won\'t be eating tonight!')
if greenpaper > cost:
	print('Yay! You can buy some nachos!')
if greenpaper == cost:
	print('That sure was lucky!')
print('Thanks for using nacho buyer.py.')
