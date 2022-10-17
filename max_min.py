# You will be given a list of integers, , and a single integer . You must create an array of length  from elements of  such that its unfairness is minimized. Call that array . Unfairness of an array is calculated as max(arr) - min(arr)

#  example:
arr = [2, 5, 9, 18, 22, 23]
k = 3


# def calcperm(arr, k): # com ajuda da internet
#     perm = list([[]])
#     for _i in range(k):
#         temp = list()
#         for tuples in perm:
#             for int in arr:
#                 if int not in tuples:
#                     curr_temp = list(tuples)
#                     curr_temp.append(int)
#                     temp.append(tuple(curr_temp))
#         perm = temp
#     return set(perm)


# fiz, mas nao passou completamente
# def maxMin(k, arr):
#     permutations = calcperm(arr, k)
#     unfairness = max(arr) - min(arr)

#     for tuple in permutations:
#         curr_unfairness = max(tuple) - min(tuple)
#         if curr_unfairness < unfairness:
#             unfairness = curr_unfairness
#     return unfairness


#  ajuda do forum
def maxMin(k, arr):
    lower_fairness = max(arr) - min(arr)
    arr.sort()
    for i in range(len(arr) - k):
        highest = arr[i+k-1]  # para pegar k elementos (menos um pois é não inclusivo)
        lowest = arr[i]
        lower_fairness = min(lower_fairness, highest - lowest)
    return lower_fairness


# def maxMin(k, arr):
#     arr.sort()
#     return min(arr[i+k-1] - arr[i] for i in range(len(arr) - k))


print(maxMin(k, arr))
