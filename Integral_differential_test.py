import numpy as np
from scipy.misc import derivative
from scipy.integrate import quad


def calc_equations(us):
    a = np.array([[2, 4], [3, 9]])
    g = np.linalg.solve(a, right_part(us))
    return g


def right_part(us):
    us = us ** 2
    b = np.array([us, 6])
    return b


def derivative_lena(us):
    d = derivative(calc_equations, us, dx=1e-6)
    return d


print(calc_equations(5))

print(derivative_lena(5))
x1 = 0
x2 = 2
Integral = quad(lambda us: derivative_lena(us)[0], 0, 2)[0]
#
print(Integral)
