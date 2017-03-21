start = True
contacts = {}
while start:
    print('Welcome to Contacts!')
    print('What would you like to do?')
    print('(1) Add a phone number.')
    print('(2) Print the full list of contacts.')
    print('(3) Enter a name to retrieve that contact\'s phone number.')
    print('(4) Enter a name to change that contact\'s phone number.')
    print('(5) Enter a name to delete that contact\'s phone number.')
    print('(0) Exit the Contacts app')
    
    response = input() 
    if response == 1:
        print('What\'s the name of your contact?')
        name = raw_input()
        print('What\'s the phone number of your contact?')
        num = raw_input()
        contacts[name] = num
    if response == 2:
        print(contacts)
    if response == 3:
        print('Whose number would you like?')
        name = raw_input()
        print('OK, here\'s the number:')
        print (contacts[name])
    if response == 4:
        print('Whose number would you like to change?')
        name = raw_input()
        print('What is the new number?')
        num = raw_input()
        contacts[name] = num
    if response == 5:
        print('Whose number would you like to del?')
        name = raw_input()
        del contacts[name]
        print('Hope it wasn\'t a bad breakup')
    if response == 0:
        start = False
    