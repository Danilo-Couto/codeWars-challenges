# import numpy as np
# arr = np.array([[0, 1, 4, 2],
#                 [4, 2, 0, 1],
#                 [2, 2, 1, 0],
#                 [3, 4, 5, 3]])

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix arr  is shown below:

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]]

# The left-to-right diagonal = 15 . The right to left diagonal = 17. Their absolute difference is 2.


def diagonalDifference(arr):
    a = []
    b = []
    for index in range(len(arr)):
        line = arr[index]
        a.append(line[index])
        b.append(line[len(line)-index-1])
    return abs(sum(a) - sum(b))


print(diagonalDifference(arr))