"""
В этом задании Вы должны найти минимум функций с помощью градиентного спуска.

Вам на вход подаются функция func, ее производная deriv (*), а также начальная точка start, на выходе - точка локального минимума. Для вашего удобства мы написали функцию для отрисовки траектории градиентного спуска

(*) - вам не нужно будет ее вычислять. То, что вы написали в предыдущем задании, вам пригодится чуть позже.

В первой реализации градиентного спуска можете предполагать, что на вход подаются функции с единственным, глобальным минимумом. Перед тем, как писать код, ответьте себе на следующие вопросы:

    Как понять, что пора остановиться? Это может зависеть от градиента или расстояния между двумя соседними шагами алгоритма, так и от числа уже выполненных итераций.
    Как правильно менять величину шага (learning rate) от итерации к итерации?

"""


def grad_descent_v1(func, deriv, start=None, callback=None):
    """ 
    Реализация градиентного спуска для функций с одним локальным минимумом,
    совпадающим с глобальным. Все тесты будут иметь такую природу.
    :param func: float -> float — функция 
    :param deriv: float -> float — её производная
    :param start: float — начальная точка
    """
    
    def deriv_func(func, x, epsilon):
        return (func(x+epsilon) - func(x))/epsilon
    
    
    max_iter = 10**5
    precision = 10**-4
    learning_rate = 0.01
    iteration = 0
    if start is None:
        # Если точка не дана, сгенерируем случайную
        # из стандартного нормального распределения.
        # При таком подходе начальная точка может быть
        # любой, а не только из какого-то ограниченного диапазона
        np.random.seed(179)
        start = np.random.randn()

      # не забывайте логировать шаги!
    
    # YOUR CODE
    
    while iteration < max_iter:
      #estimate = start
      estimate =start
      start = estimate-learning_rate * deriv_func(func,estimate,  precision)
      callback(start, func(estimate))
      iteration +=1
    return start
