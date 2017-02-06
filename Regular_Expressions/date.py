import re

def extractDate(inputString):
	regex = r'[a-zA-Z]+\s[1-3][0-9]\,\s[1-9][0-9]+'
	match = re.search(regex, inputString)
	if match:
		return match.group()

inputString = 'The date is June 10, 2017.'
print(extractDate(inputString))

'''
	that regex is very easy to break aka not good 
'''