import math, random
from timeit import default_timer as timer
import plotly as py


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

def measureTime(algorithm, list):
    times = []
    for _ in range(10):
        start = timer()
        algorithm(list, random.randint(0, len(list)*2))
        end = timer()
        times.append((end-start)*1000)
    return (sum(times)/len(times))

list10 = random.sample(range(20), 10)
list100 = random.sample(range(200), 100)
list1k = random.sample(range(2000), 1000)
list10k = random.sample(range(20000), 10000)
list100k = random.sample(range(200000), 100000)
list1mil = random.sample(range(2000000), 1000000)
list10mil = random.sample(range(20000000), 10000000)

linearSearch10Average = measureTime(linearSearch, list10)
linearSearch100Average = measureTime(linearSearch, list100)
linearSearch1kAverage = measureTime(linearSearch, list1k)
linearSearch10kAverage = measureTime(linearSearch, list10k)
linearSearch100kAverage = measureTime(linearSearch, list100k)
linearSearch1milAverage = measureTime(linearSearch, list1mil)
linearSearch10milAverage = measureTime(linearSearch, list10mil)

linearTimes = [
    linearSearch10Average,
    linearSearch100Average,
    linearSearch1kAverage,
    linearSearch10kAverage,
    linearSearch100kAverage,
    linearSearch1milAverage,
    linearSearch10milAverage
]

list10.sort()
list100.sort()
list1k.sort()
list10k.sort()
list100k.sort()
list1mil.sort()
list10mil.sort()

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

sizes = [10, 100, 1000, 10^4, 10^5, 10^6, 10^7]

lineaSearchLine = go.Scatter(
    x = sizes
)
