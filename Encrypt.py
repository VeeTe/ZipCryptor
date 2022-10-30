import os
import random
import time
with open("keys", "r") as openFile:
	lines = openFile.read().split("\n")
intCounter1 = len(lines)

strFileToEncrypt = "1.txt"
strOldFilename = strFileToEncrypt
intCounter1 = 0
for strItem in lines:
	strRandom = str(random.randint(0, 999999))
	strOutFilename = strRandom + ".zip"
	strCommand = "zip --password " + strItem + " " + strOutFilename + " " + strOldFilename
	
	#os.system("pwd")
	os.system(strCommand)
	strCommand = "shred -fuz -n 3 " + strOldFilename
	if (strOldFilename != strFileToEncrypt) and intCounter1 != (len(lines)-1): os.system(strCommand)
	intCounter1 +=1
	print(intCounter1)
	strOldFilename = strOutFilename
#	time.sleep(5)

