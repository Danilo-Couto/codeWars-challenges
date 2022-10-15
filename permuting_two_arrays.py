# Given two arrays of equal size n and an integer k. The task is to permute both arrays such that sum of their corresponding element is greater than or equal to k i.e a[i] + b[i] >= k. The task is print “Yes” if any such permutation exists, otherwise print “No”.

# Examples: Input:
import re


A = [2, 1, 3] 
B = [7, 8, 9] 
k = 10
# Output : Yes


def twoArrays(k, A, B):
    A.sort()  # [1, 2, 3]
    B.sort(reverse=True)  # [9, 8, 7]

    for i, v in enumerate(A):
        if v + B[i] < k:
            return 'NO'
    return 'YES'


print(twoArrays(k, A, B))
