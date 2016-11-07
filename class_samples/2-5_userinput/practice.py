print('How much does it cost you for a Coke?')
cost = raw_input()
print('How many Cokes will you drink today?')
cokes = raw_input()

money = int(cost) * int(cokes)
print('Wow, you\'re going to spend ' + str(money) + ' dollars on sugar water today!')
