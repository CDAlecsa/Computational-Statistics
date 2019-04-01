# %%%
'''
                            Python Packages
'''

import numpy as np
import matplotlib.pyplot as plt


# %%%
'''
                            Approximating PI (circle of a given radius plot)
'''

plt.figure()

N = 4000
r = 2
x = np.random.uniform(-r, r, N)
y = np.random.uniform(-r, r, N)

Index = y ** 2 <= r ** 2 - x ** 2
plt.plot( x[Index], y[Index],'bo')
plt.plot( x[np.invert(Index)], y[np.invert(Index)],'ro')
plt.title('Approximation of PI')

PiValue = 4 * len(x[Index]) / N
print('Approx. Pi : ', PiValue)



# %%%
'''
                            Approximating a given function by Monte Carlo method
'''

plt.figure()

N = 10000
f = lambda x : x * np.cos(71*x) + np.sin(13*x)
Ox = np.linspace(0, 1, 100)

x = np.random.uniform(0, 1, N)
y = np.random.uniform(min(f(x)), max(f(x)), N)

indexBelow = y < f(x)
indexAbove = y>= f(x)

plt.scatter(x[indexBelow], y[indexBelow], color = "green", label = 'Below the function')
plt.scatter(x[indexAbove], y[indexAbove], color = "blue", label = 'Above the function')
plt.plot(Ox, f(Ox), 'k', linewidth = 5)

plt.legend(loc = 'lower left', ncol = 2, fontsize = 12)
plt.show()

