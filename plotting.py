import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def agresti_coull(f,n):
    f = f + 2
    n = n + 4
    p_fail = f/n
    error_bar = 2*np.sqrt((p_fail*(1-p_fail))/n)
    return p_fail, error_bar

def line(x,m,c):
    return 10**(m*x + c)

x = np.array([14,18,24,32,34,36,38,40])

#p = 0.00046
fails_and_trials = np.array([[6643,100000000],
                             [1281,100000000],
                             [242,100000000],
                             [59,100000000],
                             [77,200000000],
                             [36,100000000],
                             [29,100000000],
                             [34,144000000]])

y = np.array([agresti_coull(d[0],d[1])[0] for d in fails_and_trials])
y_err = np.array([agresti_coull(d[0],d[1])[1] for d in fails_and_trials])

popt, pcov = curve_fit(line,x[-5:],y[-5:])

fit_x = [32,42,52,62,72,82,92]
fit_y = [line(i,popt[0],popt[1]) for i in fit_x]

plt.errorbar(x[:4],y[:4],y_err[:4],marker='o',color='b',linestyle='--',markerfacecolor='none')
plt.errorbar(x[4:],y[4:],y_err[4:],marker='o',color='b',linestyle='')
plt.plot(fit_x,fit_y,color='b',)
plt.xlabel(r'$L$')
plt.ylabel(r'$p_{fail}$')
plt.yscale('log')
plt.show()
