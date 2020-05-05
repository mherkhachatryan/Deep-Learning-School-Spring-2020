"""
На вход дан двумерный массив XXX. Напишите функцию, которая для каждой строчки x=(x1,x2,…,xn)x = (x_1, x_2, \ldots, x_n)x=(x1​,x2​,…,xn​) массива XXX строит строчку s=(s1,s2,…,sn)s = (s_1, s_2, \ldots, s_n)s=(s1​,s2​,…,sn​), где sk=x1+...+xks_k=x_1+...+x_ksk​=x1​+...+xk​, а затем выдаёт массив из построенных строчек. Используйте библиотеку numpy (вам поможет функция cumsum). Выходом функции должен быть двумерный массив той же формы, что и XXX.
"""

import numpy as np

def cumsum(A):
    #param A: np.array[m,n]
    #YOUR CODE

    result = np.cumsum(A, axis = 1)
    return result
