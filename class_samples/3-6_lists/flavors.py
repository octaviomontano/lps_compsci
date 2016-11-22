print 'These are our ice creams:'

flavors = ['Chocolate', 'Vanilla', 'Strawberry', 'Salted Caramel', 'Mint Chip']
print flavors

print 'Want to add an ice cream flavor? Enter it now:'
choice = raw_input()
flavors.append(choice)

print 'Great! Here\'s our menu:'

for kind in flavors:
	print kind
