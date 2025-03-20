import random

myList = []
while len(myList) < 6:
    rnd = random.randint(1, 49)
    if rnd not in myList:
        myList.append(rnd)
myList.sort()
print(myList)
