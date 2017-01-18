def mergeSort(inputList):
	if len(inputList) <= 1:
		return inputList
	middle = len(inputList)//2
	left = mergeSort(inputList[:middle])
	right = mergeSort(inputList[middle:])
	return merge(left, right)

def merge(left, right):
	output = []
	leftIndex = 0
	rightIndex = 0
	while leftIndex < len(left) and rightIndex < len(right):
		if left[leftIndex] < right[rightIndex]:
			output.append(left[leftIndex])
			leftIndex+=1
		else:
			output.append(right[rightIndex])
			rightIndex+=1
	if leftIndex < len(left):
		for x in left[leftIndex:]:
			output.append(x)
	if rightIndex < len(right):
		for x in right[rightIndex:]:
			output.append(x)
	return output


l = [1,5,8,2,3,90,452,4,231]
print(mergeSort(l))