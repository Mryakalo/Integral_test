from scipy.integrate import dblquad


def f1(x_f1, a_f1):
    return a_f1 * x_f1 ** 2


def f2(y_f1, b_f1):
    return b_f1 * y_f1


a = 2
b = 2
Integral = dblquad(lambda y, x: f2(y, b) * f1(x, a), 1, 8, lambda y: 0, lambda y: 1)
# В интеграле запись от внутреннего аргумента к внешнему, а в пределах интегрирования наоборот

print(Integral)
