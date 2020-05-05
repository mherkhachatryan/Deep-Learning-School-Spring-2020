"""
Напишите две функции, каждая из которых перемножает две квадратные матрицы: одна без использования встроенных функций numpy, а другая --- с помощью numpy. На вход первой задаче подаются списки размера size по size элементов в каждом. На вход второй задаче подаются объекты типа np.ndarray --- квадратные матрицы одинакового размера. 

Первая функция должна возвращать список списков, а вторая -- np.array.
"""

import numpy as np

def no_numpy_mult(first, second):
    """
    param first: list of "size" lists, each contains "size" floats
    param first: list of "size" lists, each contains "size" floats
    """
    size = len(first)
    result = [ [0 for _ in range(size)] for _ in range(size) ]
    #YOUR CODE: please do not use numpy
    for m in range(size):
        for n in  range(size):
            for k in range(size):
                result[m][n] += first[m][k] * second[k][n]
    
    return result

def numpy_mult(first, second):
    """
    param first: np.array[size, size]
    param second: np.array[size, size]
    """
    
    #YOUR CODE: please use numpy

    result = np.matmul(np.array(first), np.array(second))
    return result
