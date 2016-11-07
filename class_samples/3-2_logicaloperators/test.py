print('What hour is it in New York?')
NewYorkHours = raw_input()
print('What minute is it in New York?')
NewYorkMinutes = raw_input()
NewYorkTime = NewYorkHours + ':' + NewYorkMinutes
CaliforniaHours = int(NewYorkHours)
if int(NewYorkHours) >= 4:
        CaliforniaHours -= 3
if int(NewYorkHours) <= 3:
        CaliforniaHours += 9
CaliforniaTime = str(CaliforniaHours) + ':' + NewYorkMinutes
print('If the time in New York is ' + NewYorkTime + ', then the time in California is ' + CaliforniaTime)
