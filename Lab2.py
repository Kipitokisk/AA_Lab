import time
import matplotlib.pyplot as plt
import numpy as np
import random

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sorted = mergeSort(left)
    right_sorted = mergeSort(right)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    sorted_arr = arr.copy()
    for i in range(n//2, -1, -1):
        heapify(sorted_arr, n, i)
    for i in range(n-1, 0, -1):
        sorted_arr[i], sorted_arr[0] = sorted_arr[0], sorted_arr[i]
        heapify(sorted_arr, i, 0)
    return sorted_arr

def countingSort(arr):
    size = len(arr)
    output = [0] * size
    max_element = max(arr)
    count = [0] * (max_element + 1)
    for m in range(0, size):
        count[arr[m]] += 1
    for m in range(1, max_element + 1):
        count[m] += count[m - 1]
    m = size - 1
    while m >= 0:
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1
    result = [0] * size
    for m in range(0, size):
        result[m] = output[m]
    return result

def calculate_execution_time(sort_func, arr):
    start_time = time.time()
    sorted_arr = sort_func(arr)
    end_time = time.time()
    return end_time - start_time, sorted_arr

def plot_graph(execution_times, labels):
    x = np.arange(len(execution_times))
    plt.bar(x, execution_times, align='center', alpha=0.5)
    plt.xticks(x, labels)
    plt.ylabel('Execution Time (s)')
    plt.title('Sorting Algorithm Execution Times')
    plt.tight_layout()
    plt.show()

sizes = [1000, 2000, 3000, 4000, 5000]
sort_functions = [quicksort, mergeSort, heapSort, countingSort]
sort_names = ['Quicksort', 'Merge Sort', 'Heap Sort', 'Counting Sort']
execution_times = {name: [] for name in sort_names}

for size in sizes:
    arr = generate_random_array(size)
    for sort_func, name in zip(sort_functions, sort_names):
        time_taken, _ = calculate_execution_time(sort_func, arr.copy())
        execution_times[name].append(time_taken)

for name, times in execution_times.items():
    print(f"{name}: {times}")

for name, times in execution_times.items():
    plt.plot(sizes, times, label=name)

plt.xlabel('Array Size')
plt.ylabel('Execution Time (s)')
plt.title('Sorting Algorithm Execution Times')
plt.legend()
plt.show()
