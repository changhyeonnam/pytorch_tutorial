import numpy as np

'''
numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
:   Return evenly spaced values within a given interval.
    Values are generated within the half-open interval [start, stop)
    For integer arguments the function is equivalent to the Python built-in range function, 
    but returns an ndarray rather than a list. 
'''

n = np.arange(3)
print(n)

n = np.arange(3.0)
print(n)

n = np.arange(3,7)
print(n)

n = np.arange(3,7,2)
print(n)
