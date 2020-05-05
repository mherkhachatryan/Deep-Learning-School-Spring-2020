"""


С помощью numpy написать функцию для кодирования массива (Run-length encoding). Все подряд повторения элементов функция сжимает в один элемент и считает количество повторений. Функция возвращает кортеж из двух векторов одинаковой длины. Первый содержит элементы, а второй — сколько раз их нужно повторить.

Пример: encode(np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])) = (np.array([1, 2, 3, 1, 5, 2, 3]), np.array([1, 2, 2, 2, 2, 1, 2]))

"""

import numpy as np

def encode(a):
    #YOUR CODE
    from itertools import groupby 
    original = []
    occurances = []
    for key, group in groupby(a):
        occurances.append(len(list(group)))
        original.append(key)
    return (np.array(original), np.array(occurances))
