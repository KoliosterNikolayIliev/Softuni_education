import timeit


# compute linear search time
def merge_sort_time():
    SETUP_CODE = '''
from merge_sort import mergeSort
'''

    TEST_CODE = '''
arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)

    '''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=100000)

    # priniting minimum exec. time
    print(f'merge_sort time: {min(times)}')


def quick_sort_time():
    SETUP_CODE = '''

from quick_sort import quickSort, partition
'''

    TEST_CODE = '''
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
quickSort(arr, 0, n - 1)
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=100000)

    # priniting minimum exec. time
    print(f'quick_sort time: {min(times)}')


merge_sort_time()
quick_sort_time()
