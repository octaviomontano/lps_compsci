def my_max(myList):
        myList.sort()
        myList.reverse()
        return myList[0]

p = 2

if my_max([4, 5]) != None:
        l = [1, 9, -4, 130]
        if my_max(l) == 130:
                print("Nice work on the challenge, it passes!")
        else:
                print("Good work attempting the challenge, but your function fails.")

