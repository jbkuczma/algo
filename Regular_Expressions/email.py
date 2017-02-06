import re

def extractEmail(inputString):
	match = re.search(r'[\w.-]+@[\w.-]+', inputString)
	if match:
		return match.group()

testString = 'My email is: testing5@fake_gmail.com'
print(extractEmail(testString))

'''
	Regular Expression meaning: r'[\w.-]+@[\w.-]+'
		* r'___'
			represents a raw string
		* \w
			represents a char (a-z, A-Z, 0-9)
		* [\w.-]+
			represents one or more occurences of a char, '.', or '-'
		* [\w.-]+@[\w.-]+
			represents one or more occurences of a char, '.', or '-'
			BEFORE and AFTER a '@'

	prints:
		> testing5@fake_gmail.com
'''