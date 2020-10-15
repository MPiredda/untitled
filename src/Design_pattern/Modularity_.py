## FILE mymodule.py
import math
name = 'my first module!'
_privateName = 'my SECRET name!'

def _computeDelta(a,b,c):
    return b**2 - 4*a*c

def computeRealRoots(a,b,c):
    """
    compute real roots of (a x^2 + b x +c)
    """
    delta= _computeDelta(a,b,c)
    if delta>=0:
        delta_sqrt=math.sqrt(delta)
        x1= (-b - delta_sqrt) / (2 * a)
        x2 = (-b + delta_sqrt) / (2 * a)
        return x1, x2
    else:
        return None
