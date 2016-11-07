import random
print('Welcome to Octavio\'s quest!')
print('Enter the name of your character: ')
name = raw_input()
print('Enter strength (1-10):')
strength = int(raw_input())
print('Enter health (1-10)')
health = int(raw_input())
print('Enter luck (1-10)')
luck = int(raw_input())
print('')

if strength + health + luck <= 15:
        print('Values have been assigned, ' + name +':')
        print('strength: ' + str(strength) + ', health: ' + str(health) + ', luck: ' + str(luck))
else:
        print('You gave your character too many points!')
        print('Default values have been assigned, ' + name +':')
        print('strength: 5, health: 5, luck: 5')
        strength = 5
        health = 5
        luck = 5

chance = random.randint(1,12)
print('')
choice = raw_input(name + ', you\'ve come to a fork in the road. Do you want to go left or right? Enter \'right\' or \'left\': ')
print('')

if choice == 'left':
        print (name + '! You\'ve came across a ferocious Lion on your path as it sprints towards you!')
 	if luck >= chance:
		print('Your luck has saved you, for the giant cat slipped and knocked itself out while falling on it\'s head. YOU WON!')
        elif strength >= 7:
                print('No need to fear, as your strength was high enough to slay the giant cat. YOU WON! :D')
        else:
                print('Unfortunately, you were too weak to fight the giant cat and died. You lose :(')
elif choice == 'right':
        print (name + '! The road is surrounded by high levels of polution, causing poisonous gas to cover the road!')
        print('As you go continue your path forward, you cough uncontrollably, taking away your health...')
	if luck >= chance:
		print('Your luck has saved you, for a gust of wind has cleared the air, allowing you to breath normally. YOU WON!')
        elif health >= 6:
                print('No need to fear, for you made it out with ' + str(health - 5) + ' health left! YOU WON! :D')
        else:
                print('Unfortunately, your health was too low to make it through the cloud of gas while dying on the ground.')
                print('You lose :(')
else:
        print('That\'s not one of the choices!')
print('')
