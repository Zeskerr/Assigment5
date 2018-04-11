import math

def linearSearch(arr, num):
    for i in range(len(arr)):
        if(arr[i] == num):
            return
    return

def binarySearch(arr, num):
    start = 0
    end = len(arr)
    while start < end:
        middleIndex = math.floor((start + end)/2)
        if(num > arr[middleIndex]):
            start = middleIndex + 1
        else:
            end = middleIndex
    return
