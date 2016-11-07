aDecimal = input('Give me a number to the hundredths place: ') 
#I want to just receive the decimal places
a = aDecimal % 1
#Move the the decimal back one, then remove whatever is left
b = a * 10 // 1
#Convert back to the decimal
b = b / 10 
#Then add the original whole number
b = b + int(aDecimal)
print(b)

