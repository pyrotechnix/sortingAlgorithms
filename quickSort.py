import random
import math

def quickSort(arr):
    #return array if length is 1 since assumed sorted
    if len(arr) < 2:
        return arr
    partition = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] <= partition:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quickSort(left) + [partition] + quickSort(right)


def shitSort(arr):
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    splitPoint = math.floor(len(arr) / 2)
    left, right = arr[:splitPoint], arr[splitPoint:]
    return mergeLists(mergeSort(left), mergeSort(right))

    

def mergeLists(arr1, arr2):
    newList = []
    counter = 0
    for i in range(0, len(arr1)):
        for j in range(counter, len(arr2)):
            if arr2[j] < arr1[i]:
                newList.append(arr2[j])
                counter += 1
        newList.append(arr1[i])
    return(newList + arr2[counter:])


def main():
    randArray = []
    for i in range(0, 20):
        randArray.append(random.randint(0, 100))
    #print(randArray)
    array = [3, 2, 5, 1, 3, 2, 5]
    quickSortedArray = quickSort(randArray)
    print('sorted')
    print(mergeSort(randArray))
    randArray.sort()
    print(randArray == quickSortedArray)
    

main()
