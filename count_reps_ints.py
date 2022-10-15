# Dado um array de inteiros, numbers, conte o número de elementos que aparecem mais de uma vez.
 
# Exemplo
numbers = [1, 3, 3, 4, 4, 4, 5, 5, 1]
 
# Existem dois elementos não únicos: 3 e 4.
 
# Complete a função countDuplicate no editor abaixo.
 
# Retorno: int: um inteiro que denota a quantidade elementos que se repetem no array numbers.


def countDuplicate(numbers):
    reps = 0
    dup_set = set()
    numbers.sort()

    for index in range(len(numbers)-1):
        if numbers[index] == numbers[index+1] and numbers[index] not in dup_set:
            reps += 1
        dup_set.add(numbers[index])
    return reps


print(countDuplicate(numbers))