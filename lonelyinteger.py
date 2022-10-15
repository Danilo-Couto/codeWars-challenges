# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example
a = [1,2,3,4,3,2,1]

# The unique element is 4.


def lonelyinteger(array):
    rep_list = []
    for a in array:
        rep_list.append(array.count(a))
    index_of_unique = rep_list.index(1)
    # print(index_of_unique)
    return array[index_of_unique]


print(lonelyinteger(a))
