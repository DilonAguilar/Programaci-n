import sympy
from sympy.abc import x

f = x**3-sympy.sin(x)*x
f2 = f.diff(x)
f3 = f.integrate(x)

