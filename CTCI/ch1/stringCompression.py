'''
	Implement a mtheod to perform baisc string compression using the counts of repeated characters. 
	Ex: aabcccccaaa -> a2b1c5a3
	If "compressed" string doesn't become smaller than the original string, return the original string.
'''

def stringCompression(inputString):

	index = 0
	outString = ''
	x = 0
	while x < len(inputString):
		consecutiveCharCount = 1
		char = inputString[x]
		if x == len(inputString)-1:
			outString+=char
			break
		if char == inputString[x+1]:
			while char == inputString[x+1]:
				consecutiveCharCount+=1
				x+=1
				if x == len(inputString)-1:
					break
			outString+=char
			outString+=str(consecutiveCharCount)
			x+=1
		else:
			outString+=char
			x+=1
	if len(outString) > len(inputString):
		return inputString
	return outString


string1 = 'aabcccccaaa'
string2 = 'aaaaaaabb'
string3 = 'abcde'
print(stringCompression(string1))
print(stringCompression(string2))
print(stringCompression(string3))


'''
	prints:
		> a2b1c5a3
		> a7b2
		> abcde
'''