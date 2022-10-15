def findZigZagSequence(a):
    n = len(a)
    a.sort()
    mid = int((n)/2)
    a[mid], a[n-1] = a[n-1], a[mid]  # swap largest to the middle 
    # reverse remaining elements
    index_left = mid + 1
    index_right = n - 2
    while (index_left <= index_right):
        a[index_left], a[index_right] = a[index_right], a[index_left]  # swap the remainings again
        index_left += 1
        index_right -= 1

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print(findZigZagSequence(a))
