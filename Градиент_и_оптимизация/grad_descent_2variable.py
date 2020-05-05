"""


А теперь все вместе!

У вас есть только функция, которую Вам отдают в качестве аргумента и вы должны найти её минимум.

Вы будете искать глобальный, у вас это должно получиться лишь потому что тут они хорошие.

Да, и еще, теперь они не одномерные, а двумерные.

Минимум нужно искать где-то на Ω=(−5,5)×(−5,5)\Omega = (-5, 5) \times (-5, 5)Ω=(−5,5)×(−5,5)
Логика написания градиентного спуска остаётся прежней.

"""

def numerical_derivative_2d(func, epsilon):
    """
    Функция для приближённого вычисления градиента функции двух переменных. 
    :param func: np.ndarray -> float — произвольная дифференцируемая функция
    :param epsilon: float — максимальная величина приращения по осям
    :return: другая функция, которая приближённо вычисляет градиент в точке
    """
    def grad_func(x):
      """
      :param x: np.ndarray — точка, в которой нужно вычислить производную
      :return: приближённое значение производной в этой точке
      """
      # YOUR CODE

      grad_x = (func(np.array([x[0]+epsilon, x[1]])) -func( np.array([x[0], x[1]])) )/epsilon
      grad_y = (func(np.array([x[0], x[1]+epsilon])) -func( np.array([x[0], x[1]])) )/epsilon
      gradient = np.array([grad_x, grad_y])
      return gradient
    return grad_func


def grad_descent_2d(func, low, high, callback=None):
    """ 
    Реализация градиентного спуска для функций двух переменных 
    с несколькими локальным минимумами, но известной квадратной окрестностью
    глобального минимума. Все тесты будут иметь такую природу.

    Обратите внимание, что здесь градиент функции не дан.
    Его нужно вычислять приближённо.

    :param func: np.ndarray -> float — функция 
    :param low: левая граница интервала по каждой из осей
    :param high: правая граница интервала по каждой из осей
    """
    precision = 10**-10
    lr = 1
    max_iter = 10**4
    gradient = numerical_derivative_2d(func, precision)
    #xx, yy = np.mgrid[low:high:0.1, low:high:0.1]
    start = np.array([low, low])
    start2 = np.array([high, high])
    for iteration in range(max_iter):
      estimate =  start
      estimate2 = start2
      start = estimate - lr*gradient(estimate)
      start2 = estimate2 - lr*gradient(estimate2)
      callback(start, func(estimate))
    if np.min(start) < np.min(start2):
      best_estimate = start
    else:
      best_estimate = start2
    #best_estimate = min(min1, min2)
    #print(start)
    # YOUR CODE
    return best_estimate
    
