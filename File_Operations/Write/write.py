def writeFile():
	with open('writeFilePython.txt', 'a') as outputFile:
		outputFile.write('Writing to a txt file with Python.')
		outputFile.close()

writeFile()

