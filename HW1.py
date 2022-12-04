# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

pi = math.pi
d_str = input('Введите точность через точку: ')

d_list = d_str.split('.')
count_d = len(d_list[1])
print(round(pi, count_d))
