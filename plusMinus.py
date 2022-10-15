# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

# Example

# There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

# 0.400000
# 0.400000
# 0.200000


def plusMinus(arr):
    length = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for int in arr:
        if int > 0:
            pos += 1
        if int < 0:
            neg += 1
        if int == 0:
            zero += 1
    print(round(pos/length, 6), '\n', round(neg/length, 6), '\n', round(zero/length, 6))


if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)
