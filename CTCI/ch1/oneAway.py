'''
	Given two strings, write a function to check if they are one edit (or zero edits) away. An edit
	is considered inserting a character, removing a character, or replacing a character.
'''

def lengthDifference(string1, string2):
	return abs(len(string1) - len(string2))

def checkReplaceOrRemove(string1, string2):
	#string1 is the bigger string
	x = 0
	y = 0
	editsMade = 0
	while x < len(string1) and y < len(string2):
		if string1[x] != string2[y]:
			editsMade+=1
			x+=1
		else:
			x+=1
			y+=1
	return editsMade


def oneAway(inputString1, inputString2):
	diff = lengthDifference(inputString1, inputString2)
	editsMade = 0
	if diff > 1:
		return False	
	# both strings are the samee size
	elif diff == 0:
		for x in range(0, len(inputString1)):
			if inputString1[x] != inputString2[x]:
				editsMade+=1
	# strings differ in length by 1
	elif diff == 1:
		if len(inputString1) > len(inputString2):
			editsMade = checkReplaceOrRemove(inputString1, inputString2)
		else:
			editsMade = checkReplaceOrRemove(inputString2, inputString1)
	if editsMade > 1:
		return False
	return True



print(oneAway('pale', 'ple'))
print(oneAway('pales', 'pale'))
print(oneAway('pale', 'bale'))
print(oneAway('pale', 'bake'))
print(oneAway('pizza', 'italy'))
print(oneAway('bus', 'backpack'))

'''
	prints:
		> True
		> True
		> True
		> False
		> False
		> False
'''