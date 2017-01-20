'''
	Write an algorithm such that if an element in an MxN matrix is 0, 
	its entire row and column are set to 0.
'''

def zeroMatrix(matrix):
	numberOfRows = len(matrix[0])
	numberOfColumns = len(matrix)
	# whereAreTheZeros = [[False for x in range(numberOfRows)] for y in range(numberOfColumns)]
	whereAreTheZeros = []
	indexInRow = 0
	currentRow = 0
	for row in matrix:
		indexInRow = 0
		for number in row:
			if number == 0:
				whereAreTheZeros.append((currentRow, indexInRow))
			indexInRow+=1
		currentRow+=1

	currentRow = 0
	for item in whereAreTheZeros:
		row = item[0]
		column = item[1]
		for x in range(len(matrix[row])):
			matrix[row][x] = 0
		for y in range(len(matrix)):
			matrix[currentRow][column] = 0
			currentRow+=1
		currentRow = 0
	return matrix

matrix = [
	[1,2,3,0],
	[1,2,2,2],
	[1,3,4,7]
]

print(zeroMatrix(matrix))
'''
	prints: 

		> [[0, 0, 0, 0], [1, 2, 2, 0], [1, 3, 4, 0]]
							|
							|
							|
				 matrix can be written as:

						[
						 [0, 0, 0, 0]
						 [1, 2, 2, 0]
						 [1, 3, 4, 0]
						]
'''

