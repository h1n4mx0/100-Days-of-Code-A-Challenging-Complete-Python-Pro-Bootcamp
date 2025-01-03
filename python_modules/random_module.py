# Random Module In Python

import random
print(dir(random))
#%%
""" List of attributes and methods available in 'random' module:
---------------------------------------------------------------------------------------
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom',
 'TWOPI', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__',
 '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate',
 '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_inst', '_log', '_os',
 '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator',
 '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate',
 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate',
 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle',
 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
---------------------------------------------------------------------------------------
"""
#%%
from random import random
print(random())

#%%
import random
print(random.random())
#%%
# random.random() is the basic function of the random module.
# This random function will return the floating point random number in [0.0, 1.0]
print(random())
#%%
# Let's see the different functions and their usage:
# 'randint'
import random
print(random.randint(10, 20))
#%%
# Run 3 times to get 3 values at the interval 3
print(random.randrange(10, 20, 3)) # Run 3 times to get 3 values
#%%
print(random.uniform(3.2, 4.5))
#%%
print(random.choice([10, 20, 30, 40, 100, 120, 150]))
#%%
print(random.sample([10, 20, 30, 40, 100, 120, 150, 160, 170], k=4))
#%%
print(random.choices([10, 20, 30, 40, 100, 120, 150, 160, 170], k=4))
#%%
x = [10, 20, 30, 40, 100, 120, 150, 160, 170]
print(random.shuffle(x))
print(x)
#%%
# How Random Seed() Function Works
import random
print(random.randint(10, 20))
print(random.randint(10, 20))
print(random.randint(10, 20))
#%%
print(random.seed(4))
print(random.randint(10, 30))
#%%
print(random.seed(48.6))
print(random.randint(10, 30))
#%%
# random.triangular(low, high, mode)
print(random.triangular(20, 50, 5))
#%%
# How to use getstate and setstate methods
# Example
import random

numbers = [10, 20, 30, 40, 100, 120, 150, 160, 170]

# Step1 print the sample from the above list of numbers
print(random.sample(numbers, k=4))

# Step2 Get the current state and store as state
state = random.getstate()

# Step3 Set current state before printing the same sample again
random.setstate(state)

# Step4 Now if we print the sample we will get the same sample as before
print(random.sample(numbers, k=4))

# Step5 Recheck by setting the state once again before printing
random.setstate(state)
print(random.sample(numbers, k=4))

# Step6 Now try to print the sample without using random.setstate(state)
random.setstate(state)
print(random.sample(numbers, k=4))
#%%
# How To Get Help From Python
# Step 1: We can use 'Help' method
#         on any object
import math
print(help(math))
#%%
# Step 2: We can use 'dir' method to
#         get list of attributes,
#         functions, classes, variables,
#         or methods
print(dir(math))
print(math.ceil(34.56))
print(math.factorial())
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

#%%

#%%

#%%

