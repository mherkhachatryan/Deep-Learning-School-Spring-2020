"""
Вам подаются на вход два вектора a и b в трехмерном пространстве. Реализуйте их скалярное произведение с помощью numpy и без. 

"""

# scalar product 
import numpy as np

def no_numpy_scalar(v1, v2):
    #param v1, v2: lists of 3 ints
    #YOUR CODE: please do not use numpy
    result = 0
    for i in range(3):
        result += v1[i]*v2[i]
    #result = #YOUR CODE
    return result

def numpy_scalar (v1, v2):
    #param v1, v2: np.arrays[3]
    #YOUR CODE

    result =np.dot(np.array(v1), np.array(v2))
    return result
