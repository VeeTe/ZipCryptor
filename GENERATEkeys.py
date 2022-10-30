import random
intCounter = 15
strArray1 = []
intLinesTotal = sum(1 for line in open("main_keys"))
while intCounter != 0:
	intRandom = random.randint(0, intLinesTotal+1)
	if False == (intRandom in strArray1):
		intCounter -=1
		strArray1.append(intRandom)
with open("main_keys", "r") as openFile:
	lines = openFile.read().split("\n")
	


fp = open("keys", 'w')
intCounter = 0
for strItem in lines:
	strNewItem = strItem + "\n"
	if intCounter in strArray1:
		fp.write(strNewItem)
	intCounter += 1
