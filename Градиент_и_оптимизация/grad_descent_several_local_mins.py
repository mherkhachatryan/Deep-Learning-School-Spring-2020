"""
Это задание чуть сложнее. Если раньше Вам нужно было просто найти минимум у довольно хорошей функции, то сейчас в тестах будут плохие. У них будет несколько минимумов и вам нужно найти глобальный у каждой функции.

В общем случае такая задача невыполнима, но у вас будут одномерные функции и все самое интересное будет сосредоточено в районе нуля. Скажем, известно что глобальный минимум лежит в пределах (low, high). Вам нужно как-то изменить градиентный спуск, который вы написали в предыдущем задании, чтобы он работал и в таком случае. Например, запускать его из нескольких случайно выбранных точек интервала и выбирать лучший ответ.

Больше о тонкостях градиентного спуска можно прочитать, например, в лекциях МФТИ.
"""

import inspect
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

def grad_descent_v2(func, deriv, low=None, high=None, callback=None):
    """ 
    Реализация градиентного спуска для функций с несколькими локальным минимумами,
    но с известной окрестностью глобального минимума. 
    Все тесты будут иметь такую природу.
    :param func: float -> float — функция 
    :param deriv: float -> float — её производная
    :param low: float — левая граница окрестности
    :param high: float — правая граница окрестности
    """
    # YOUR CODE
    #def deriv_func(func, x, epsilon):
  
    #  return (func(x+epsilon) - func(x))/epsilon


    max_iter = 10000
    precision = 10**-5
    lr = 0.001
    iteration = 0
    
    """
    if low is None:
      np.random.seed(1234)
      low = np.random.randn()
    elif high is None:
      np.random.seed(345)
      high = np.random.randn()
     """ 
   # low = low+1
   # high = high -1
    start = np.linspace(low, high,10)
    #print(start)
    # start = start[start !=0]
    #print(start)
    while iteration < max_iter:
      estimate = start
      #new_estimate = high
      #print(len(deriv_func(func, estimate, precision)))
      #print(type(deriv))
      gradient = deriv(estimate)
      gradient = gradient[gradient !=np.nan]
      start = estimate - lr * gradient
      start[start<low] = low
      start[start>high] = high
      #lr *= decay
      #callback(start, func(estimate))
      iteration +=1

    
    # print (start[start!=np.nan ])
    # start = start[start!=np.nan ]
    start = start[~np.isnan(start)]
    func_values = func(start)
    # print(f"start: {start}")
    # print(f"func values: {func_values}")
    min_indices = np.where(func_values == np.min(func_values))
    # print(min_indices)
    # print(min_indices)
    # print(min_indices)
    # print(start[min_indices[0]])
    minimum = start[min_indices[0]][0]
    #print(start)
    #print(minimum)
    #print ('{},{}, low={}, high={}'.format(inspect.getsource(func), inspect.getsource(deriv), low, high))
    return minimum
