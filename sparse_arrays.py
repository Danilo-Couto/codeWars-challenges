# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

# Example

# strings = ['ab', 'ab', 'abc']
# queries = ['ab', 'abc', 'bc']

# strings = ['aba', 'baba', 'aba', 'xzxb']
# queries = ['aba', 'xzxb', 'ab']

# There are 2 instances of 'ab', 1 of 'abc' and 0 of 'bc'. For each query, add an element to the return array, result = [2,1,0].

# Function Description

# Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

# matchingStrings has the following parameters:

# string strings[n] - an array of strings to search
# string queries[q] - an array of query strings
# Returns

# int[q]: an array of results for each query

strings = ['100','lekgdisnsbfdzpqlkg','eagemhdygyv','jwvwwnrhuai','urcadmrwlqe','mpgqsvxrijpombyv','mpgqsvxrijpombyv','urcadmrwlqe','mpgqsvxrijpombyv','eagemhdygyv','eagemhdygyv','jwvwwnrhuai','urcadmrwlqe','jwvwwnrhuai','kvugevicpsdf','kvugevicpsdf','mpgqsvxrijpombyv','urcadmrwlqe','mpgqsvxrijpombyv','exdafbnobg','qhootohpnfvbl','suffrbmqgnln','exdafbnobg','exdafbnobg','eagemhdygyv','mpgqsvxrijpombyv','urcadmrwlqe','jwvwwnrhuai','lekgdisnsbfdzpqlkg','mpgqsvxrijpombyv','lekgdisnsbfdzpqlkg','jwvwwnrhuai','exdafbnobg','mpgqsvxrijpombyv','kvugevicpsdf','qhootohpnfvbl','urcadmrwlqe','kvugevicpsdf','mpgqsvxrijpombyv','lekgdisnsbfdzpqlkg','mpgqsvxrijpombyv','kvugevicpsdf','qhootohpnfvbl','lxyqetmgdbmh','urcadmrwlqe','urcadmrwlqe','kvugevicpsdf','lxyqetmgdbmh','urcadmrwlqe','lxyqetmgdbmh','jwvwwnrhuai','qhootohpnfvbl','qhootohpnfvbl','jwvwwnrhuai','lekgdisnsbfdzpqlkg','kvugevicpsdf','mpgqsvxrijpombyv','exdafbnobg','kvugevicpsdf','lekgdisnsbfdzpqlkg','qhootohpnfvbl','exdafbnobg','qhootohpnfvbl','exdafbnobg','mpgqsvxrijpombyv','suffrbmqgnln','mpgqsvxrijpombyv','qhootohpnfvbl','jwvwwnrhuai','mpgqsvxrijpombyv','qhootohpnfvbl','lekgdisnsbfdzpqlkg','eagemhdygyv','jwvwwnrhuai','kvugevicpsdf','eagemhdygyv','eagemhdygyv','lxyqetmgdbmh','qhootohpnfvbl','lxyqetmgdbmh','exdafbnobg','qhootohpnfvbl','qhootohpnfvbl','exdafbnobg','suffrbmqgnln','mpgqsvxrijpombyv','urcadmrwlqe','eagemhdygyv','lxyqetmgdbmh','urcadmrwlqe','suffrbmqgnln','qhootohpnfvbl','kvugevicpsdf','lekgdisnsbfdzpqlkg','lxyqetmgdbmh','mpgqsvxrijpombyv','jwvwwnrhuai','lxyqetmgdbmh','lxyqetmgdbmh','lekgdisnsbfdzpqlkg','qhootohpnfvbl','100','exdafbnobg','eagemhdygyv','mpgqsvxrijpombyv','kvugevicpsdf','lekgdisnsbfdzpqlkg','kvugevicpsdf','exdafbnobg','qhootohpnfvbl','eagemhdygyv','kvugevicpsdf','suffrbmqgnln','jwvwwnrhuai','lekgdisnsbfdzpqlkg','lekgdisnsbfdzpqlkg','mpgqsvxrijpombyv','jwvwwnrhuai','kvugevicpsdf','lekgdisnsbfdzpqlkg','exdafbnobg','suffrbmqgnln','qhootohpnfvbl','eagemhdygyv','exdafbnobg','suffrbmqgnln','jwvwwnrhuai','qhootohpnfvbl','eagemhdygyv','exdafbnobg','exdafbnobg','jwvwwnrhuai','qhootohpnfvbl','lxyqetmgdbmh','qhootohpnfvbl','suffrbmqgnln','lxyqetmgdbmh','qhootohpnfvbl','eagemhdygyv','jwvwwnrhuai','eagemhdygyv','qhootohpnfvbl','mpgqsvxrijpombyv','qhootohpnfvbl','jwvwwnrhuai','exdafbnobg','eagemhdygyv','eagemhdygyv','kvugevicpsdf','kvugevicpsdf','jwvwwnrhuai','urcadmrwlqe','lxyqetmgdbmh','qhootohpnfvbl','exdafbnobg','exdafbnobg','eagemhdygyv','qhootohpnfvbl','exdafbnobg','exdafbnobg','lekgdisnsbfdzpqlkg','jwvwwnrhuai','eagemhdygyv','urcadmrwlqe','kvugevicpsdf','lekgdisnsbfdzpqlkg','jwvwwnrhuai','eagemhdygyv','lekgdisnsbfdzpqlkg','exdafbnobg','kvugevicpsdf','jwvwwnrhuai','exdafbnobg','lxyqetmgdbmh','exdafbnobg','lxyqetmgdbmh','jwvwwnrhuai','mpgqsvxrijpombyv','eagemhdygyv','urcadmrwlqe','kvugevicpsdf','qhootohpnfvbl','jwvwwnrhuai','eagemhdygyv','urcadmrwlqe','urcadmrwlqe','exdafbnobg','qhootohpnfvbl','exdafbnobg','eagemhdygyv','exdafbnobg','jwvwwnrhuai','eagemhdygyv','jwvwwnrhuai','mpgqsvxrijpombyv','urcadmrwlqe','urcadmrwlqe','eagemhdygyv','eagemhdygyv','jwvwwnrhuai','suffrbmqgnln','eagemhdygyv']

queries = list(set(strings))

def matchingStrings(strings,queries):
    q_dict = {}
    for query in queries:
        q_dict[query] = strings.count(query)

    return list(q_dict.values())


# solution from vincentkho10
def matchingStrings2(strings, queries):
    res = [0]*len(queries)
    for string in strings:
        for index, value in enumerate(queries):
            if (string==value):
                res[index]+=1
    return res


def matchingStrings3(strings, queries):
    arr = []
    for i in range(len(queries)):
        counter = 0
        for i2 in range(len(strings)):
            if queries[i] == strings[i2]:
                counter +=1
        arr.append(counter)

    return arr


print(matchingStrings(strings, queries))
print(matchingStrings2(strings, queries))
print(matchingStrings3(strings, queries))

# my solution give the same result, but not in hacker rank