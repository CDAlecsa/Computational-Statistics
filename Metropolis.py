# %%%
'''
                                Python Packages
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss



# %%%
'''
                                Metropolis algorithm
'''

def MetropolisAlgorithm(Fct, steps, stdX) :
    
    samples = np.zeros((1, steps))
    samples = samples[0]
    x_Old = Fct.mean()
    OldProbab = Fct.pdf(x_Old) 
    
    for i in range(0,steps) :
        x_New = x_Old + np.random.normal(0, stdX)
        NewProbab = Fct.pdf(x_New)
        
        AcceptanceRatio = NewProbab / OldProbab
        
        if AcceptanceRatio >= np.random.random() :
            samples[i] = x_New
            x_Old = x_New
            OldProbab = NewProbab
        else :
            samples[i] = x_Old
    
    return samples        


# %%%
'''
                                    Metropolis alg. for estimating a p.d.f.
'''
    
Fct = ss.beta(5, 1.3)
stdX = 0.2
steps = 10 ** 4
samples = MetropolisAlgorithm(Fct, steps, stdX)

x = np.linspace(0.01, .99, 100)
y = Fct.pdf(x)
plt.xlim(0, 1)
plt.plot(x, y, 'k-', lw=3, label = 'Exact distribution')
plt.hist(samples, bins = 50, normed=True, label = 'Estimated distribution')
plt.xlabel(r'$x$', fontsize = 12)
plt.ylabel(r'$f(x)$', fontsize = 12)
plt.legend(fontsize = 12) 
plt.title('Metropolis Algorithm for Estimating the pdf of a r.v.')
plt.show() 