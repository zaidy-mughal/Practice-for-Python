#this function is used to implement merge sort
def MergeSort(list,start,end):
    if (end-start)+1 < 2:
        return list
    else:
        mid = int((start+end)/2)
        MergeSort(list,start,mid)
        MergeSort(list,mid+1,end)
        Merge(list,start,mid,end)



def Merge(list,start,mid,end):
    list1Size = (mid-start)+1
    list2Size = end-mid

    left = []
    right = []

    i = start
    j = mid+1

    for i in range(list1Size):
        left.append(list[start+i])

    for j in range(list2Size):
        right.append(list[j+mid+1])

    i,j,k = 0,0,start

    while i<list1Size and j<list2Size:
        if left[i] <= right[j]:
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j]
            j += 1
        k += 1

    while i<list1Size:
        list[k] = left[i]
        k += 1
        i += 1




list = [1,5,2,6,34,7,4,2]

MergeSort(list,0,7)

print(list)











#this method is taken from AI after writing my own method from algorithm
#This method is only taken for the purpose of comparison of my code with the AI's optimised code


# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2  # Finding the mid of the array
#         L = arr[:mid]  # Dividing the array elements into 2 halves
#         R = arr[mid:]

#         mergeSort(L)  # Sorting the first half
#         mergeSort(R)  # Sorting the second half

#         i = j = k = 0

#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1

#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1

