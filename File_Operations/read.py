from sys import argv

def readFile(fileName):
	file = open(fileName, 'r')
	for line in file:
		print(line.strip())
	file.close()

'''
	Two possible ways of reading from file. Either txt file is provided via command line argument 
	or file name is provided in function call.
	
	1) readFile(argv[1]) 
	> python3 read.py read.txt

	prints:
		This
		is
		a
		test
		file

	2) readFile('read.txt')
	> python3 read.py

	prints:
		This
		is
		a
		test
		file
'''