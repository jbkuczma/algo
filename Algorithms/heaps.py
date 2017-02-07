'''
    Heap's Algorithms generates all possible permutations of n objects
'''

def heapsAlgo(theList): #to generate all permutations of a list.
    lengthOfList = len(theList)
    i = 0
    id = [0 for i in range(lengthOfList)] #create a list of zeros with a length of the list
    result = [theList]
    index = 0
    while index < lengthOfList:
        if id[index] < index:
            anotherList = list(theList)
            if id[index] % 2 == 0:
                theList[0], theList[index] = theList[index], theList[0] #swap values
            else:
                theList[id[index]], theList[index] = theList[index], theList[id[index]] #swap values
            result.append(anotherList)
            id[index] += 1
            index = 0
        else:
            id[index] = 0
            index += 1
    return result


li = [1,2,3]
print(heapsAlgo(li))