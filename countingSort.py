# Comparison Sorting
# Quicksort usually has a running time of , but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat  (worst-case) running time, since  represents the minimum number of comparisons needed to know where to place each element. For more details, you can see these notes (PDF).

# Alternative Sorting
# Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

# Challenge
# Given a list of integers, count and return the number of times each value appears as an array of integers.

arr = [1, 1, 3, 2, 1]


def countingSort(arr):
    new_arr = [0]*(max(arr)+1)
    arr_set = set()

    for value in arr:
        if value in arr_set:
            new_arr[value] += 1
        else:
            arr_set.add(value)
            new_arr[value] += 1

    return new_arr


print(countingSort(arr))