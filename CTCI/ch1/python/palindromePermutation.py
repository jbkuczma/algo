'''
	Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is
	a word or phrase that is the same forwards and backwards. A permutation is a rearragnement of letters. 
	The palindrome does not need to b elimited to just dictionary words.
'''

def checkIfPossiblePalindrome(inputString):
	letters = {}
	inputString = inputString.lower()
	for letter in inputString:
		if letter not in letters:
			letters[letter] = 1
		else:
			letters[letter]+=1

	singleInstanceOfLetter = 0
	for letter in letters:
		if letters[letter] == 1 and letter != ' ':
			singleInstanceOfLetter+=1

	return singleInstanceOfLetter <= 1

def palindromePermutation(inputString):
	return checkIfPossiblePalindrome(inputString)

string1 = 'Tact Coa'
string2 = 'Able was I ere I saw Elba'
string3 = 'random Words'
print(palindromePermutation(string1))
print(palindromePermutation(string2))
print(palindromePermutation(string3))

'''
	prints:
		> True
		> True
		> False
'''