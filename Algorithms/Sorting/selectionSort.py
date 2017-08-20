def selectionSort(li):
	for i in range(len(li)):
		smallest = i
		for j in range(i+1, len(li)):
			if li[j] < li[smallest]:
				smallest = j

		swap(li, smallest, i)
	return li

def swap(li, x, y):
	temp = li[x]
	li[x] = li[y]
	li[y] = temp


li = [12,4.5,1,0.5,1248,57,1230,55.55,879,0.1,0,5467.1]
print(selectionSort(li))

'''
	prints:
		[0, 0.1, 0.5, 1, 4.5, 12, 55.55, 57, 879, 1230, 1248, 5467.1]
'''
