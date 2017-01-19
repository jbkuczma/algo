'''
	Write a method to replace all spaces in a string with '%20'. You can assume you are given the 'true'
	length of the string
'''

def URLify(inputString, length):
	return inputString.replace(' ', '%20')




string1 = 'Mr John Smith'
print(URLify(string1, 13))
'''
	prints:
		> Mr%20John%20Smith
'''