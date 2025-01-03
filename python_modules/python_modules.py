# Python Built-in Modules
# To see the Python Built-in Modules use help method
#%%
# 'modules' library
help('modules')
#%%
# List of Important Modules Used By The Programmer @intermediate
# and @advanced level
"""
[copy, datetime, dateutil, importlib,abc, io,
 array,jupyter, jupyterlab, keyword, calendar,
 cmd, math, matplotlib, numpy, os, pandas,pip,
 seaborn, scipy, regutil, regutil, re, random
 nltk, string,symbol, sympy, sys, sysconfig,
 time, turtle, twisted, zipp,
 ]
"""
#%%
# Let's Work On Math Module
import math
print(help(math))
#%%
print(dir(math))
"""
[ '__doc__', '__loader__', '__name__', '__package__', '__spec__',
 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil',
 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf',
 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp',
 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf',
 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p',
 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod',
 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau',
 'trunc', 'ulp' ]
"""
#%%
# Let's see the documentation of Math Module Using '__doc__' method
print(math.__doc__)
print(math.__package__)
print(math.__name__)
print(math.__loader__)
print(help('import'))
#%%
# 'ceil'
print(math.ceil(5.7))
print(math.ceil(5.45))
#%%
# 'floor'
print(math.floor(5.7))
print(math.floor(5.45))
#%%
# 'factorial'
print(math.factorial(6))
#%%
# 'gcd'
print(math.gcd(20, 50))
print(math.gcd(20, 55))
#%%
# 'fabs'
print(math.fabs(5.78))
print(math.fabs(-5.78))
#%%
# 'exp'
print(math.exp(3))
print(math.exp(-5))
print(math.exp(0.0))
#%%
# 'pow'
print(math.pow(5, 2))
print(math.pow(9, 0.5))
#%%
# 'log'
print(math.log(5, 2))
#%%
# 'log2'
print(math.log2(5))
#%%
# 'log10'
print(math.log10(5))
#%%
# 'log1p'
print(math.log1p(5))
#%%
# 'sqrt'
print(math.sqrt(81))
print(math.sqrt(0))
print(math.sqrt(1))
print(math.sqrt(4.5))
print(math.sqrt(-1)) # We will get an error
#%%
# Trigonometric Functions
# 'pi'
print(math.pi)
#%%
# 'sin()'
print(math.sin(math.pi/2))
print(math.sin(math.pi/6))
print(math.sin(0))
print(math.sin(math.pi))
#%%
# 'cos()'
print(math.cos(math.pi/2))
print(math.cos(math.pi/6))
print(math.cos(0))
print(math.cos(math.pi))
#%%
# 'tan()'
print(math.tan(math.pi/2))
print(math.tan(math.pi/6))
print(math.tan(0))
print(math.tan(math.pi))
#%%
# Converting From Degrees To Radians & Radians To Degrees
# 'pi' --> is in Radian in Math Module.
print(math.pi)

# Radians To Degree
print(math.degrees(math.pi/6))  # Approximately 30 Degree

# Degrees To Radians
print(math.radians(30))
#%%

# Important Special Functions
# 'gamma'
print(math.gamma(8))
#%%
# 'isinf()'
print(math.isinf(math.pi))
print(math.isinf(math.e))
print(math.isinf(math.inf))
print(math.isinf(float('inf')))
print(math.isinf(float('-inf')))
#%%
# 'isnan()'
print(math.isnan(math.pi))
print(math.isnan(math.e))
print(math.isnan(math.inf))
print(math.isnan(float('nan')))
#%%
# 'copysign()'
print(math.copysign(3, -4))
#%%
# 'fmod'
print(math.fmod(7, 5))
#%%
# 'frexp'
print(math.frexp(7))
#%%
# 'fsum'
print(math.fsum([1, 2, 3, 4, 5, 6, 7]))
#%%
# 'isfinite'
print(math.isfinite(float('inf')))
print(math.isfinite(float('nan')))
print(math.isfinite(math.e))
print(math.isfinite(math.pi))
#%%
# 'ldexp'
print(math.ldexp(3, 2))
#%%
# 'modf'
print(math.modf(7))
#%%
# 'trunc'
print(math.trunc(5.556))
print(math.trunc(5.335))
#%%
# To Get Inverse Values For The 'cos', 'sin', & 'tan'
# We use | 'acos', 'asin', 'atan'| and | 'atan2(x, y)--> atan2(x/y)'|
print(math.pi/2)
print(math.acos(math.cos(math.pi/2)))
print(math.asin(math.sin(math.pi/4)))
print(math.atan(math.sin(math.pi/4)))
#%%
# To Get The Values Of Hyperbolic 'cos', 'sin', and 'tan'
# We Use | sinh(), cosh(), tanh() |
print(math.sinh((math.pi/2)))
print(math.cosh((math.pi/2)))
print(math.tanh((math.pi/2)))
#%%
# To Get The Values Of Inverse Hyperbolic 'cos', 'sin', and 'tan'
# We Use | asinh(), acosh(), atanh() |
#%%
# We Can Also Get Useful Constant Values From Math Module
print(math.e)
print(math.pi)
print(math.tau)
print(math.inf)
print(-math.inf)
print(math.inf < 10e20)
print(math.inf > 10e20)
print(math.nan)
print(float('nan'))
#%%

#%%


#%%

#%%

#%%

#%%

#%%

#%%


#%%

#%%

#%%

#%%

#%%

#%%


#%%

#%%

#%%