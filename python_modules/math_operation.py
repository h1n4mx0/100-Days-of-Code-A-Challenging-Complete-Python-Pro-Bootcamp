# This is "math_operation" module (Means a scrift file with definitions, classes & statements)
# Let's create some variables to use in another module <module_intro>

math_funct_list = ['Addition', 'Subtraction', 'Division', 'Multiplication', 'Power Operation']
some_values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#%%
# Modification
# Let's create user defined function as math_function
def math_function():
    print("This is math_function under math_operation module")
    num1 = int(input("Enter nume1: "))
    num2 = int(input("Enter nume2: "))
    addition = num1 + num2
    subtraction = num1 - num2
    division = num1 / num2
    multiplication = num1 * num2
    # return addition, subtraction, division, multiplication