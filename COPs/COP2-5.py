import numpy as np


def chebypts(a, b, n):
  a_pts = np.arange(1, n+1)
  x = (b+a)/2 + 0.5*(b-a)*np.cos(((2*a_pts - 1)/(2*n))*np.pi)
  return x


a = -7
b = 6
n = 5

cheb = chebypts(a, b, n)


def errSimple(c, l, f): return np.abs(
    np.prod([(c - pt) for pt in l]))*np.abs(f(c))/np.math.factorial(l.shape[0])


def errCheb(a, b, f, c, n): return np.abs(
    (((b-a)/2)**n)/(2**(n-1)))*np.abs(f(c))/np.math.factorial(n)


def fx(x): return np.exp(x)


print(errCheb(a, b, fx, b, n))

xlin = np.linspace(-1, 1, 5)
print(errSimple(-0.25, xlin, fx))
