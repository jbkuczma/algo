def binarySearch(sortedList, value):
	low = sortedList[0]
	high = sortedList[len(sortedList) - 1]
	while low <= high:
		mid = (low + high)//2
		if mid > value:
			high = mid-1
		elif mid < value:
			low = mid+1
		else:
			return mid
	return -1

def binarySearchRecursive(sortedList, value, low = 0, high = -1):
	if high == -1:
		high = len(sortedList) - 1
	mid = (low + high)//2
	if low > high:
		return -1
	if sortedList[mid] > value:
		return binarySearchRecursive(sortedList, value, low, mid-1)
	elif sortedList[mid] < value:
		return binarySearchRecursive(sortedList, value, mid+1, high)
	else:
		return mid


l = [0,1,2,3,4,5,6,7,8,9]

print(binarySearch(l, 3))
print(binarySearchRecursive(l, 3))
