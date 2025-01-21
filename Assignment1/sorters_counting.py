import numpy as np

# Initialize counters for insertion sort
counters_is = np.zeros(2)

def insertion_sort(data):
    """
    Perform insertion sort on the given data.
    Counters:
    counters_is[0] - number of outer loop iterations
    counters_is[1] - number of inner loop iterations
    """
    for i in range(1, len(data)):
        counters_is[0] += 1
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            counters_is[1] += 1
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# Initialize counters for merge sort
counters_ms = np.zeros(4)

def merge_sort(data):
    """
    Perform merge sort on the given data.
    Counters:
    counters_ms[0] - number of recursive calls
    counters_ms[1] - number of comparisons in merge
    counters_ms[2] - number of left array insertions
    counters_ms[3] - number of right array insertions
    """
    counters_ms[0] += 1

    # check if data has more than one element (not sorted)
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        # call merge_sort on left and right arrays
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            counters_ms[1] += 1
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        # fill the data with remaining left elements
        while i < len(left):
            counters_ms[2] += 1
            data[k] = left[i]
            i += 1
            k += 1

        # fill the data with remaining right elements
        while j < len(right):
            counters_ms[3] += 1
            data[k] = right[j]
            j += 1
            k += 1
    return data

# Initialize counters for heap sort
counters_hs = np.zeros(3)

def heapify(data, n, i):
    """
    Helper function to maintain the heap property.
    Counters:
    counters_hs[2] - number of heapify calls
    """
    counters_hs[2] += 1
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[i] < data[left]:
        largest = left

    if right < n and data[largest] < data[right]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)

def heap_sort(data):
    """
    Perform heap sort on the given data.
    Counters:
    counters_hs[0] - number of heapify calls during build heap
    counters_hs[1] - number of heapify calls during sort
    """
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        counters_hs[0] += 1
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        counters_hs[1] += 1
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)

    return data

# Initialize counters for quick sort
counters_qs = np.zeros(4)

def partition(data, low, high):
    """
    Helper function to partition the array for quick sort.
    Counters:
    counters_qs[2] - number of partition calls
    counters_qs[3] - number of comparisons in partition
    """
    counters_qs[2] += 1
    i = low - 1
    pivot = data[high]

    for j in range(low, high):
        counters_qs[3] += 1
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1, data

def quick_sort_helper(data, low, high):
    """
    Recursive helper function for quick sort.
    Counters:
    counters_qs[1] - number of recursive calls
    """
    counters_qs[1] += 1
    if low < high:
        pi, data = partition(data, low, high)
        quick_sort_helper(data, low, pi - 1)
        quick_sort_helper(data, pi + 1, high)
    return data

def quick_sort(data):
    """
    Perform quick sort on the given data.
    Counters:
    counters_qs[0] - number of initial quick sort calls
    """
    counters_qs[0] += 1
    data = quick_sort_helper(data, 0, len(data) - 1)
    return data

if __name__ == '__main__':
    # Number of measurements
    meas_count = 25
    # Number of sorting algorithms
    num_of_sorts = 4
    # Initialize a matrix to store counters for all sorts
    counters_all = np.zeros((num_of_sorts, meas_count))
    # Scale factor for data length
    scale = 1.4
    # Initial data length
    datalen = 5

    for i in range(meas_count):
        # Increase data length
        datalen = np.floor(datalen * scale).astype(int)
        # Generate random data array from 0 to datalen of length datalen
        data = np.random.randint(0, datalen, datalen)
        
        # Perform sorting and collect counters
        insertion_sort(data.copy())
        merge_sort(data.copy())
        heap_sort(data.copy())
        quick_sort(data.copy())

        # Store the results
        counters_all[0, i] = counters_is.sum()
        counters_all[1, i] = counters_ms.sum()
        counters_all[2, i] = counters_hs.sum()
        counters_all[3, i] = counters_qs.sum()

        # Reset the counters
        counters_is = np.zeros(2)
        counters_ms = np.zeros(4)
        counters_hs = np.zeros(3)
        counters_qs = np.zeros(4)

    # Print the results
    print(f'Insertion Sort Counters: {counters_all[0, :]}')
    print(f'Merge Sort Counters: {counters_all[1, :]}')
    print(f'Heap Sort Counters: {counters_all[2, :]}')
    print(f'Quick Sort Counters: {counters_all[3, :]}')





