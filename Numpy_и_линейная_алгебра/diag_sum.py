"""


Напишите функцию, которая находит сумму четных элементов на главной диагонали квадратной матрицы (именно чётных элементов, а не элементов на чётных позициях!). Если чётных элементов нет, то вывести 0. Используйте библиотеку numpy.

"""

import numpy as np
def diag_2k(a):
    #param a: np.array[size, size]
    #YOUR CODE
    diagonal = a.diagonal()
    result = sum(filter(lambda x: x%2 == 0, diagonal))
    return result
