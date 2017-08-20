def bubbleSort(inputList):
    size = len(inputList)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(inputList)):
            if(inputList[i-1] > inputList[i]):
                swap(inputList, i-1, i)
                swapped = True
    return inputList


def swap(li, i, j):
    temp = li[i]
    li[i] = li[j]
    li[j] = temp

l = [1,5,8,2,3,90,452,4,231]
print(bubbleSort(l))