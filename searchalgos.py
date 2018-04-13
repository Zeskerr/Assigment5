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
            print('Number {0} was found in position {1}'.format(num, middle))
            return
    return

#measures average time for search algorithm in ms for 10 iterations
def measureTime(algorithm, list):
    times = []
    for _ in range(10):
        start = timer()
        algorithm(list, random.randint(0, len(list)*2))
        end = timer()
        times.append((end-start)*1000)
    return (sum(times)/len(times))

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
linearSearch10Average = measureTime(linearSearch, list10)
linearSearch100Average = measureTime(linearSearch, list100)
linearSearch1kAverage = measureTime(linearSearch, list1k)
linearSearch10kAverage = measureTime(linearSearch, list10k)
linearSearch100kAverage = measureTime(linearSearch, list100k)
linearSearch1milAverage = measureTime(linearSearch, list1mil)
linearSearch10milAverage = measureTime(linearSearch, list10mil)

linearSearchTimes = [
    linearSearch10Average,
    linearSearch100Average,
    linearSearch1kAverage,
    linearSearch10kAverage,
    linearSearch100kAverage,
    linearSearch1milAverage,
    linearSearch10milAverage
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
binarySearch10Average = measureTime(binarySearch, list10)
binarySearch100Average = measureTime(binarySearch, list100)
binarySearch1kAverage = measureTime(binarySearch, list1k)
binarySearch10kAverage = measureTime(binarySearch, list10k)
binarySearch100kAverage = measureTime(binarySearch, list100k)
binarySearch1milAverge = measureTime(binarySearch, list1mil)
binarySearch10milAverge = measureTime(binarySearch, list10mil)

binarySearchTimes = [
    binarySearch10Average,
    binarySearch100Average,
    binarySearch1kAverage,
    binarySearch10kAverage,
    binarySearch100kAverage,
    binarySearch1milAverge,
    binarySearch10milAverge
]

for i in range(len(linearSearchTimes)):
    print('The average time for linear search is {0}ms'.format(linearSearchTimes[i]))
for i in range(len(binarySearchTimes)):
    print('The average time for binary search is {0}ms'.format(binarySearchTimes[i]))

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
