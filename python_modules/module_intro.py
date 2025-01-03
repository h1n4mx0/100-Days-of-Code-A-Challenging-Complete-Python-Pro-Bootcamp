# Python Modules Introduction
# In Python, there are two types of modules.

# Built-in Modules
# User-defined Modules
# Some commonly used Python built-in modules are | datetime, os, math, sys, random |
# Importing the whole module
# To import modules in Python, we use the Python "import" keyword.
# Syntax: import <module name>

import math
#%%
# To import multiple modules, we can put each modules name saparated by commas.
# Syntax: import <module name1>, <module name2>, ....... <module nameN>
import datetime, os, sys
#%%
# Import only specific classes or functions from a module
# Attribute Method
# Syntax: <module name>.<class Or Function name>
squareOf7 =  math.sqrt(7)
print(squareOf7)
#%%
# From Method
# Syntax: from <module name> import <class Or function name>
from math import sqrt
squareOf8 = sqrt(8)
print(squareOf8)
#%%
# Import with renaming a module ( Callled as aliasing the original name of the module or  class)
# Syntax: from <module name> import <class or function name> as <alias name>
from math import sqrt as sq
squareOf9 = sq(9)
print(squareOf9)
# Syntax : import <module name> as <alias name>
import random as rand
print(rand.randrange(10, 30, 2))
#%%
# Import all names
# Syntax: from <module name> import *
from math import *
print(pow(5,2))
print(factorial(5))
print(pi)
print(sqrt(200))
#%%
# Create Module
# Let's create a module name called "math_operation" in the current directory or folder
# After creating the module import it here to use its objects
# Let's import the module and use its variables
import math_operation
print("Printing the math_funct_list and some values used in the module <math_operation>")
math_functions = math_operation.math_funct_list 
values = math_operation.some_values
print(math_functions)
print(values)
#%%
import sys
print(sys.path)
#%%
# When we update a module, we have to use the "reload()" function from importlib method
# Step1: So, let's modify the module "math_operation" 
# Step2: Go to math_operation and modify with user defined function
# Step3: After modification try to call the module objects WITHOUT reload

from math_operation import math_function 
add_operation = math_function.addition
sub_operation = math_function.subtraction
div_operation = math_function.division
mul_operation = math_function.multiplication
print(add_operation)
print(sub_operation)
print(div_operation)
print(mul_operation)
#%%
# After modification try to call the module objects WITH reload
from importlib import reload
reload(math_operation)
from math_operation import math_function 
add_operation, sub_operation, div_operation, mul_operation = math_function()
# math_function
# sub_operation = math_function().subtraction
# div_operation = math_function().division
# mul_operation = math_function().multiplication
print(add_operation)
print(sub_operation)
print(div_operation)
print(mul_operation)
#%%
# The dir() function
# In Python, dir() is a built-in function. This function is used to list all members of the
# current module.
# We have imported math module; So, we can see all the attributes, functions and methods
from importlib import reload
reload(math_operation)
dir(math_operation)
print(dir(math))

import sys
print(dir(sys))
print(sys.version)
print(dir())
#%%
# Similarly If we want to see the list of Python builtin functions and attributes
# we can use Python builtins module
import builtins
print(dir(builtins))
#%%
# We also have several other builtin Modules like datetime, random etc
# importing built in module random
import random

# printing random integer between 0 and 10
print(random.randint(0, 10))
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
