# diaryFinder.py asks the user for a path to a directory,
# scans that directory for txt files,
# reads the files, looking for the word 'Diary',
# --assuming that a Diary file would include words like
# "Dear Diary"... for the presentation's sake.
# If it finds your diary, it prints it to the screen,
# then copies it for later perusal.

import os

path = raw_input("Type the full path to the directory you wish to scan.\n")

os.system("dir /b " + path + " > aTemporaryPythonFile.txt")
#use os module's system function to run "dir /b" on the given path
#and store it in a temporary file in the current working directory.

f = open("aTemporaryPythonFile.txt", "r")
#now we use python's reknowned text processing capabilities 
#to act upon that list of files.

dirString = f.read() #the read() method returns the file's entire contents.
f.close() #the file doesn't need to be open any longer.
os.system("erase aTemporaryPythonFile.txt") #clean up.
dirList = dirString.split() #instead of a long string, we want a list.

print("\nHere are the files in that directory:\n")
for x in dirList:
	if x[-4:] == r'.txt' or x[-4:] == r'.TXT':
		print(x)
	else:
		pass
print("\n")
#now we find which files end in .txt, and read their contents.
for x in dirList:
	if x == r'aTemporaryPythonFile.txt':
		pass #we already erased this file, so we better not try to open it.

	elif x[-4:] == r'.txt' or x[-4] == r'.TXT':
		f = open(path + "\\" + x,"r")
		buffer = f.read()
		f.close()
		#we use the always useful "for y in range(len(x))" formulation
		#to act as a fast, pseudo-grep command:
		for y in range(len(buffer)):
			if len(buffer[y:]) < 5:
				pass
			elif buffer[y:y+5] == 'Diary':
				print("Found a Diary File!!\nLet's read it, and copy it!\n")
				print(buffer)
				os.system("copy " + path + "\\" + x + " DiaryCopy.txt")
				break
			else:
				pass
		f.close()
	else:
		pass
