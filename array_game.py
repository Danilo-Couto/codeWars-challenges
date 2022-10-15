# Dado um array de inteiros, determine o número de movimentos necessários para tornar todos os elementos
# iguais. Cada movimento consiste em escolher todos menos um dos elementos do array e incrementar seus
# valores em 1. 

# Exemplo 

# numbers = [3, 4, 6, 6, 3] 
# Escolha 4 dos 5 elementos durante cada movimento e incremente cada um dos seus valores por um. Para 
# este caso são necessários 7 movimentos, como mostrado a seguir: 
 
# Índice do elemento 
#     Iteração      Array         não alterado 
#     0    [ 3,  4,  6,  6,  3]             
#     1    [ 4,  5,  7,  6,  4]    3 
#     2    [ 5,  6,  7,  7,  5]    2 
#     3    [ 6,  7,  8,  7,  6]    3 
#     4     [ 7,  8,  8,  8,  7]    2 
#     5    [ 8,  9,  9,  8,  8]    3 
#     6    [ 9,  9, 10,  9,  9]    1 
#     7    [10, 10, 10, 10, 10]    2 

numbers = [3, 4, 6, 6, 3]

# def minMoves(numbers):
#     size = len(numbers)
#     answer = 0

#     while len(set(numbers)) != 1:
#         max_index = numbers.index(max(numbers))
#         for index in range(size):
#             if index != max_index:
#                 numbers[index] += 1
#         answer += 1
#     return answer


# def minMoves(numbers):  #[3, 4, 6, 6, 3]
#     min_number = min(numbers)
#     answer = 0

#     for index in range(len(numbers)):
#         answer += numbers[index] - min_number
#     return answer


# eu que fiz, quase certo:
def minMoves(numbers):
    numbers.sort(reverse=True)  # [6, 6, 4, 3, 3]
    size = len(numbers)
    iterations = 0

    while len(set(numbers)) != 1:
        for index in range(size-1):
            if numbers[index] != numbers[index+1]:
                numbers[index+1] += 1
                iterations += 1
    return iterations


print(minMoves(numbers))
