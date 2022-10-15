# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

# There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .


# def sockMerchant(n, ar):
#     pair_dict = {i: round(ar.count(i)//2) for i in ar}.values()
#     return sum(pair_dict.values())

def sockMerchant(ar):
    return sum({i: round(ar.count(i)//2) for i in ar}.values())


print(sockMerchant(ar))