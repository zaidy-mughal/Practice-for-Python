#this function performs binary search on sorted list

def findMiddle(sortedList):
    if len(sortedList)%2==0:
        return int((len(sortedList)/2)-1)
    else:
        return int(len(sortedList)/2)


def binarySearch(data,sortedList):

    middleIndex = findMiddle(sortedList)

    if data == sortedList[middleIndex]:
        return True
    if data < sortedList[middleIndex]:
        return binarySearch(data,sortedList[:middleIndex])
    if data > sortedList[middleIndex]:
        return binarySearch(data,sortedList[middleIndex:])
    else:
        return False 


list = [1,2,3,4,5,6,7]
print(binarySearch(3,list))
    
    
    

