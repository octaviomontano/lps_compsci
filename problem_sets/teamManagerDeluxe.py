import pickle
class TeamMember(object):
  def __init__(self, name, age, goals, jnum, position):
    self.name = name
    self.age = age
    self.goals = goals
    self.jnum = jnum
    self.position = position
  
  #view stats of player
  def getStats(self):
    stats = 'Name: ' + self.name + '\n'
    stats += 'Age: ' + str(self.age) + '\n'
    stats += 'Goals: ' + str(self.goals) + '\n'
    stats += 'Jersey Number: ' + str(self.jnum) + '\n'
    stats += 'Position: ' + self.position + '\n'
    return stats 

  #returns player goals
  def getGoals(self):
    return int(self.goals)
  
  #returns player age
  def getAge(self):
    return int(self.age)
  
#returns team into program
def loadTeam():
    print('What\'s the filename for your existing team? Enter the whole name, including its .tmd extension.')
    filename = raw_input()
    with open(filename, 'r') as x:
      return pickle.load(x)
    

#saves team to file
def saveTeam():
    print('What\'s the filename would you call team? Enter the whole name, adding a .tmd extension')
    filename = raw_input()
    with open(filename,'wb') as x:
      pickle.dump(myPlayers, x)

#creates empty list to store player data  
myPlayers = []

# user interface
keepRunning = True
#loop that asks for user input

print('Welcome to Team Manager Deluxe! \n Do you want to start with a new team or open an existing team? \n Enter the # of your choice and press Enter. \n (1) Start with a new team \n (2) Open a file for an existing team')
choice = input()
  
if choice == 2:
  myPlayers = loadTeam()

while keepRunning:
  print("What would you like to do? Enter the # of your choice and press 'enter' \n (1) Add a player. \n (2) Print all players. \n (3) Print average number of goals for all players \n (4) Print average age for all players \n (5) Save your player list to a file \n (0) Leave the program")
  response = input()
  
  #statement that breaks the loop and ends the program
  if response == 0:
    keepRunning = False
    
  #prompts detail for new player
  if response == 1:
    print('Enter name:')
    name = raw_input()
    print('Enter age:')
    age = input()
    print('Enter number of goals scored this season:')
    goals = input()
    print('Enter player Jersey Number:')
    jnum = input()
    print('Enter player position:')
    position = raw_input()
    print('Okay, player entered. \n')
    #creates new object and adds it to the list
    newPlayer = TeamMember(name, age, goals, jnum, position)
    myPlayers.append(newPlayer)

  if response == 2:
    print('\n')
    #retrieves & prints all the stats
    for p in myPlayers:
      print(p.getStats())

  if response == 3:
    total = 0
    #adds all the goals together and returns the average
    for p in myPlayers:
      total += p.getGoals()
    print(total/len(myPlayers))

  if response == 4:
    total = 0
    #adds all the ages together and returns the average
    for p in myPlayers:
      total += p.getAge()
    print(total/len(myPlayers)) 

  if response == 5:
    saveTeam()