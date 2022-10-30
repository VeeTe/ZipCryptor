#This proggo outputs a list of values into a file


CharacterLength = 5

openFile = open("Characters", "r")
your_list = openFile.read()

import random
intCounter = 26
strArray1 = []
strCharlist = ""
while intCounter != 0:
	intRandom = random.randint(0, len(your_list)+1)
	if False == (intRandom in strArray1) and (your_list[intRandom] != " "):
		intCounter -=1
		strArray1.append(intRandom)
		strCharlist += your_list[intRandom]
		

your_list = strCharlist
complete_list = []
for current in range(CharacterLength):
    a = [i for i in your_list]
    for y in range(current):
        a = [x+i for i in your_list for x in a]
    complete_list = complete_list+a

#print(complete_list)
#exit()
intLinesTotal = 0
fp = open("main_keys", 'w')
for strItem in complete_list:
        # write each item on a new line
	if len(strItem) >= (CharacterLength-1):
		strNewItem = strItem + "\n"
		fp.write(strNewItem)
		intLinesTotal += 1
print(intLinesTotal)

