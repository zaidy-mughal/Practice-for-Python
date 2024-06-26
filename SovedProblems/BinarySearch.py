#this function performs binary search on sorted list


def binarySearch(data,sortedList):
    low = 0
    high = len(sortedList)-1

    while low <= high:
        
        middle = int((low+high)/2)

        if data < sortedList[middle]:
            high = middle-1
        elif data > sortedList[middle]:
            low = middle+1
        else:
            return middle
        
    return -1


    

list = [1,2,3,4,5,6,7]
index = binarySearch(8,list)
if index == -1:
    print('Value Not Found')
else:
    print(print('Index of searched Element is: ',index))
    
    
    

