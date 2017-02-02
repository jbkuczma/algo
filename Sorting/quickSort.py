def quickSort(li, start, end):
	if start < end:
		pivot = partition(li, start, end)
		quickSort(li, start, pivot-1)
		quickSort(li, pivot+1, end)
	return li

def partition(li, start, end):
	pivot = li[start]
	left = start+1
	right = end
	finished = False
	while not finished:
		while left <= right and li[left] <= pivot:
			left+=1
		while li[right] >= pivot and right >= left:
			right-=1
		if right < left:
			finished = True
		else:
			temp = li[left]
			li[left] = li[right]
			li[right] = temp
	temp = li[start]
	li[start] = li[right]
	li[right] = temp
	return right


li = [7,2,6,12,98,45,1009,452,192,0,432,879]
print(quickSort(li, 0, len(li)-1))
'''
	prints:
		[0, 2, 6, 7, 12, 45, 98, 192, 432, 452, 879, 1009]
'''