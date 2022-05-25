from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import quad


def integrand(x): return 1/np.sqrt(4-x**2)


x = np.linspace(1/6, 1/2, 100)

lower_lim = 1/6
upper_lim = 1/2

integral, integral_error = quad(integrand, lower_lim, upper_lim)

print("result of integration is: ", integral)
print("result of integration-error is: ", integral_error)


################################################################

# with Simpson's rule

N = int(input("please enter a integer number as N: "))


def simps(f, a, b, N=50):
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a, b, N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S


res = simps(lambda x: 1/np.sqrt(4-x**2), 1/6, 1/2, N)

print("result of integration with simpson's rule is: ", res)


plt.plot(integral, color="red")
plt.plot(x, integrand(x), color="purple")
plt.xlabel("Limit")
plt.ylabel("Integration of Function")
plt.grid()
plt.show()
