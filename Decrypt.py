import os
import random

with open("keys", "r") as openFile:
	lines = openFile.read().split("\n")
intCounter1 = len(lines)
lines.pop()
lines.reverse()


for strItem in lines:
	os.system("find *.zip>lastzip.txt")
	with open('lastzip.txt', 'r') as openFile: 
		strArray1 = openFile.readlines()
#		print(strArray1)
	for strItem1 in strArray1:
		strCommand = "unzip -qq -d . -P '" + strItem + "' " + strItem1.replace("\n","")
#		print(strCommand)
		os.system(strCommand)
os.system("shred -fuz -n 3 *.zip")
os.system("shred -fuz -n 3 lastzip.txt")


