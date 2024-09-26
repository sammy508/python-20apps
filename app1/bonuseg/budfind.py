"""
Bug-Fixing Exercise 1
The following formula calculates the free-fall time of an object.

t= sq.root(2h/g)


def calculate_time(g=9.80665, h):  here non default paarmeter 'h' should comes first then default parameter
    t = (2 * h / g) ** 0.5
    return t
    
  
time = calculate_time(100)
print(time)
"""
# After bug fix

import math
def calculate_time(h,g=9.806):
    t = (2*h)/g 
    math.sqrt(t)
    return t
time = calculate_time(100)
print(time)
    