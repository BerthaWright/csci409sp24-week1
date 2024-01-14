### Program
''' Bertha Wright: Program 2-2
Date: 13-Nov-2022
Assignment: Week 12
Pseudocode: None Needed
'''
### Main Program

# Sort
import random

# Time import was being weird, so I had to keep importing for some reason

data_set = random.sample(range(1, 32_001), k=1000)
value = data_set[random.randint(1, 1000) - 1]

sort_time_list = []
for i in range(0, 10):
    import time

    start = time.time()

    copy_data_set = data_set.copy()
    data_set_sort = copy_data_set.sort()

    num = 0
    for x in range(1, 10000):
        num += x
    end = time.time()

    time = end - start
    sort_time_list.append(time)
sort_average = sum(sort_time_list) / len(sort_time_list)
print("The average time for the Sort Method is", sort_average, end=" seconds \n")

# Sorted

sorted_time_list = []
for i in range(0, 10):
    import time

    start = time.time()
    # Pycharm kept saying this: AttributeError: 'list' object has no attribute 'sorted' so I assumed you ment the sorted
    # function
    sorted_data_set = sorted(data_set)

    num = 0
    for x in range(1, 10000):
        num += x
    end = time.time()
    time = end - start
    sorted_time_list.append(time)

sorted_average = sum(sorted_time_list) / len(sorted_time_list)
print("The average time of the Sorted Function is", sorted_average, end=" seconds")


# This is where I got this sorting algorithm: https://www.geeksforgeeks.org/sorting-algorithms-in-python/
# Bubble


def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found
            # is greater than the adjacent element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubble_time_list = []
for i in range(0, 10):
    import time

    start = time.time()
    bubbleSort(data_set)

    num = 0
    for x in range(1, 10000):
        num += x
    end = time.time()
    time = end - start
    bubble_time_list.append(time)

bubble_average = sum(bubble_time_list) / len(bubble_time_list)
print("\nThe average time of the Bubble Sort is", bubble_average, end=" seconds")

# It looks like the Sort Method is fantastic in terms of efficiency. It is the fastest sorting method that is in this
# module. The times are pretty consistent. The Sort Method ranges from 0.0006447 - 0.00089 seconds. It usually stayed
# within the 0.00064 range. The Sorted Function ranges from 0.0006448 - 0.00074, so it is a little more consistent
# than the Sort Method, but I ran the code five times and calculated the average of the averages and the sort method
# is a little faster with an average of 0.00069282 and the Sorted Function had an average of 0.00069288 seconds. So the
# Sort Method is faster by just a bit. The Bubble Sort was the worst in terms of efficiency. it ranged from 0.025 -
# 0.032 seconds.
