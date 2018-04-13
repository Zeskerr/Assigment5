import math, random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from matplotlib import interactive

#linear search no need for return value only measuring time
def linearSearch(arr, num):
    for i in range(len(arr)):
        if(arr[i] == num):
            return
    return

#binary search no need for return value only measuring time
def binarySearch(arr, num):
    start = 0
    end = len(arr) - 1
    while(end > start):
        middle = (start + end) // 2
        if(arr[middle] > num):
            end = middle - 1
        elif(arr[middle] < num):
            start = middle + 1
        else:
            return
    return

#measures average time for search algorithm in ms for 10 iterations
def measureTime(algorithm, list):
    times = []
    for _ in range(10):
        start = timer()
        algorithm(list, random.sample(range(len(list)*2), 1)[0])
        end = timer()
        time = (end - start) * 1000
        times.append(time)
    return(sum(times)/len(times))

#generating random lists
#random.sample(x, n) will generate a list of random values from 0 to x without replacement of length n
list10 = random.sample(range(20), 10)
list100 = random.sample(range(200), 100)
list1k = random.sample(range(2000), 1000)
list10k = random.sample(range(20000), 10000)
list100k = random.sample(range(200000), 100000)
list1mil = random.sample(range(2000000), 1000000)
list10mil = random.sample(range(20000000), 10000000)

#average time values for linear search for lists of length from 10 to 10 million by increments of 10
linearSearch10 = measureTime(linearSearch, list10)
linearSearch100 = measureTime(linearSearch, list100)
linearSearch1k = measureTime(linearSearch, list1k)
linearSearch10k = measureTime(linearSearch, list10k)
linearSearch100k = measureTime(linearSearch, list100k)
linearSearch1mil = measureTime(linearSearch, list1mil)
linearSearch10mil = measureTime(linearSearch, list10mil)

linearSearchTimes = [
    linearSearch10,
    linearSearch100,
    linearSearch1k,
    linearSearch10k,
    linearSearch100k,
    linearSearch1mil,
    linearSearch10mil
]

#sorting previously generated lists in increasing order for binary search
list10.sort()
list100.sort()
list1k.sort()
list10k.sort()
list100k.sort()
list1mil.sort()
list10mil.sort()

#average time values for binary search
binarySearch10 = measureTime(binarySearch, list10)
binarySearch100 = measureTime(binarySearch, list100)
binarySearch1k = measureTime(binarySearch, list1k)
binarySearch10k = measureTime(binarySearch, list10k)
binarySearch100k = measureTime(binarySearch, list100k)
binarySearch1mil = measureTime(binarySearch, list1mil)
binarySearch10mil = measureTime(binarySearch, list10mil)

binarySearchTimes = [
    binarySearch10,
    binarySearch100,
    binarySearch1k,
    binarySearch10k,
    binarySearch100k,
    binarySearch1mil,
    binarySearch10mil
]

for i in range(len(linearSearchTimes)):
    print('The execution times for linear search is {0}ms'.format(linearSearchTimes[i]))
for i in range(len(binarySearchTimes)):
    print('The execution times time for binary search is {0}ms'.format(binarySearchTimes[i]))

#text representation of list sizes
sizes = ['10', '100', '1000', '10^4', '10^5', '10^6', '10^7']

#plotting linear search times
plt.figure(1)
plt.plot(sizes, linearSearchTimes)
plt.ylabel('Time (ms)')
plt.xlabel('List size')
plt.title('Linear Search Algorith')
interactive(True)
plt.show()

#plotting binary search times
plt.figure(2)
plt.plot(sizes, binarySearchTimes)
plt.ylabel('Time (ms)')
plt.xlabel('List size')
plt.title('Binary Search Algorithm')
interactive(False)
plt.show()
