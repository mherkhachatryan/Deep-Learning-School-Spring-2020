"""
Реализуйте класс "Нейрон", у которого будет несколько методов:

     __init__. Принимает на вход массив весов нейрона --- w=(w1,…,wn)w = (w_1, \ldots, w_n)w=(w1​,…,wn​), а также функцию активации fff (аргумент по умолчанию f(x)=xf(x) = xf(x)=x). Сохраняет веса и функцию внутри класса.
    forward. Принимает на вход массив x=(x1,…,xn)x = (x_1, \ldots, x_n)x=(x1​,…,xn​) --- входы нейрона. Возвращает f(w1x1+…+wnxn)f(w_1x_1 + \ldots + w_nx_n)f(w1​x1​+…+wn​xn​).
    backlog. Возвращает массив xxx, который подавался на вход функции forward при её последнем вызове. Если ранее функция forward не вызывалось, возвращает None.

"""



import numpy as np


class Neuron:

    def __init__(self, w, f=lambda x: x):
        # YOUR CODE HERE
        self.w = w
        self.f = f

    def forward(self, x):
        self.x = x
        return self.f(np.dot(np.array(self.x), np.array(self.w)))

    def backlog(self):
        return self.x