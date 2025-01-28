import numpy as np


##################### INSERTION SORT #####################
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
        # pick the element to insert
        num2instert = data[i]
        j = i - 1
        # insert the element in the correct position
        while j >= 0 and num2instert < data[j]:
            counters_is[1] += 1
            # "bubble" the element to the right
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = num2instert
    return data

def worst_data_is(n):
    """
    Generate the worst case data for insertion sort.
    """
    return np.arange(n, 0, -1)

##################### MERGE SORT #####################
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
        # get the middle index and split the data into left and right arrays
        middle_idx = np.floor(len(data)/2).astype(int)
        left = data[:middle_idx]
        right = data[middle_idx:]

        # call merge_sort on the left and right arrays
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

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

##################### HEAP SORT #####################
# Initialize counters for heap sort
counters_hs = np.zeros(3)

def worst_data_ms(n):
    """
    Generate the worst case data for merge sort.
    Note that the worst case data for merge sort is 
    the same as the best case data. This is because
    the while loops will in sum always run the same number 
    of times.
    """
    return np.random.randint(0, n, n)

def heapify(data, n, i):
    """
    Helper function to maintain the heap property.
    Counters:
    counters_hs[2] - number of heapify calls
    """
    counters_hs[2] += 1
    # get the indices of the left and right children
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[i] < data[left]:
        largest = left

    if right < n and data[largest] < data[right]:
        largest = right

    # swap the root with the largest child if needed
    if largest != i:
        largest_val = data[largest]
        data[largest] = data[i]
        data[i] = largest_val
        # recursively heapify the affected sub-tree
        heapify(data, n, largest)

def heap_sort(data):
    """
    Perform heap sort on the given data.
    Counters:
    counters_hs[0] - number of heapify calls during build heap
    counters_hs[1] - number of runs in while during extracting sorted values
    """
    n = len(data)
    # get the sorted heap
    for i in range(np.floor(n/2).astype(int) - 1, -1, -1):
        counters_hs[0] += 1
        heapify(data, n, i)

    # sort the array by using the heap property
    for i in range(n - 1, 0, -1):
        counters_hs[1] += 1
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
    return data

def worst_data_hs(n):
    """
    Generate the worst case data for heap sort.
    """
    return np.arange(n, 0, -1)

##################### QUICK SORT #####################
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

    # iterate through the array and swap elements if needed
    # the change depends on the pivot value
    for j in range(low, high):
        counters_qs[3] += 1
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1, data

def qs_recursive(data, low, high):
    """
    Recursive helper function for quick sort.
    Counters:
    counters_qs[1] - number of recursive calls
    """
    counters_qs[1] += 1
    if low < high:
        # partition the array using pivot
        pi, data = partition(data, low, high)
        # recursively call quick sort on the 
        # partitioned left and right sub-arrays
        qs_recursive(data, low, pi - 1)
        qs_recursive(data, pi + 1, high)
    return data

def quick_sort(data):
    """
    Perform quick sort on the given data.
    Counters:
    counters_qs[0] - number of initial quick sort calls
    """
    counters_qs[0] += 1
    data = qs_recursive(data, 0, len(data) - 1)
    return data

def worst_data_qs(n):
    """
    Generate the worst case data for quick sort.
    """
    return np.arange(0, n, 1)

def is_sorted(data):
    """
    Check if the given data is sorted.
    """
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True

if __name__ == '__main__':
    # Number of measurements
    meas_count = 25
    # Number of sorting algorithms
    num_of_sorts = 4
    # Initialize a matrix to store counters for all sorts
    counters_all = np.zeros((num_of_sorts, meas_count))
    # Scale factor for data length
    scale = 1.1
    # Initial data length
    datalen = 50

    for i in range(meas_count):
        # Increase data length
        datalen = np.floor(datalen * scale).astype(int)
        ''' 
        generate worst case data for every algorithm and test it
        '''
        # insertion sort
        data = worst_data_is(datalen)
        if not is_sorted(insertion_sort(data)):
            print('Insertion Sort failed')
        
        # merge sort
        data = worst_data_ms(datalen)
        if not is_sorted(merge_sort(data)):
            print('Merge Sort failed')

        # heap sort
        data = worst_data_hs(datalen)
        if not is_sorted(heap_sort(data)):
            print('Heap Sort failed')

        # quick sort
        data = worst_data_qs(datalen)        
        if not is_sorted(quick_sort(data)):
            print('Quick Sort failed')

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





