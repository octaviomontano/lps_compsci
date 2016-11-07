#Starting off by taking inputs
print('What hour is it in New York?')
NewYorkHours = raw_input()
print('What minute is it in New York?')
NewYorkMinutes = raw_input()
#Then Create the time in New York
NewYorkTime = NewYorkHours + ':' + NewYorkMinutes
#Convert to integers so I can do math
CaliforniaHours = int(NewYorkHours)
#Made certain conditions so that the math can be done properly according to the hour
if int(NewYorkHours) >= 4:
        CaliforniaHours -= 3
if int(NewYorkHours) <= 3:
        CaliforniaHours += 9
#Then create the time in California
CaliforniaTime = str(CaliforniaHours) + ':' + NewYorkMinutes
#Outputitng results
print('If the time in New York is ' + NewYorkTime + ', then the time in California is ' + CaliforniaTime)
