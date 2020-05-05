"""
Дан массив A[0,…,N−1]A[0,\ldots,N-1]A[0,…,N−1]. Реализуйте функцию cumsum_and_erase(...), принимающую один обязательный аргумент AAA и один опциональный аргумент eraseerase erase, по умолчанию равный 1 и возвращающую массив B[0,…,M−1]B[0,\ldots, M-1]B[0,…,M−1], где Bi=A0+…+AiB_i = A_0 + \ldots + A_{i}Bi​=A0​+…+Ai​ --- массив частичных сумм массива AAA, предварительно удалив из массива BBB все элементы, равные параметру eraseerase erase.

Постарайтесь сделать это за время O(N)O(N)O(N) без использования Numpy.

Пример работы функции:

A = [5, 1, 4, 5, 14]
B = cumsum_and_erase(A, erase=10)
assert B == [5, 6, 15, 29], "Something is wrong! Please try again"

"""

def cumsum_and_erase(A, erase = 1):
    #YOUR CODE
    total = 0
    B = []
    for x in A:
        total += x
        B.append(total)
    B = list(filter(lambda x: x!=erase, B))
    return B