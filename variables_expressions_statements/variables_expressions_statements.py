Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(5)
5
>>> print("Hello Engineer")
Hello Engineer
>>> type(5)
<class 'int'>
>>> type("Hello Engineer")
<class 'str'>
>>> type(2.0)
<class 'float'>
>>> print('20')
20
>>> print('20.5')
20.5
>>> type('20')
<class 'str'>
>>> type('20.5')
<class 'str'>
>>> # VARIABLES
>>> message = "We are Engineers"
>>> n = 17
>>> pi = 3.141592
>>> message
'We are Engineers'
>>> print(message)
We are Engineers
>>> print(n)
17
>>> print(pi)
3.141592
>>> type(message)
<class 'str'>
>>> type(n)
<class 'int'>
type(pi)
<class 'float'>
x = 10
print(x)
10
x = 20
print(x)
20
x = 30
print(x)
30
a = 10
type(a)
<class 'int'>
a = "ABC"
type(a)
<class 'str'>
# UNDEFINED VARIABLE OR UNBOUND VARIABLE
x = 2
x
2
y
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    y
NameError: name 'y' is not defined
# Delete the Variables
del x
x
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    x
NameError: name 'x' is not defined
# IDENTIFIERS
x = 2
x2 = 3
total = x + x2
port_22 = 2
# Invalid Identifiers
sub-total = 3
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
first entry = 4
SyntaxError: invalid syntax
4all = 5
SyntaxError: invalid decimal literal
*4 = 3
SyntaxError: cannot assign to literal
if = 3
SyntaxError: invalid syntax
class = 5
SyntaxError: invalid syntax
IF = 3
IF
3
Class = 5
# Statements In Python
x = 3
x
3
print(x)
3
# Operators And Operands
# +, -, *, /, and **
# Addition
20 + 30
50
30 - 5 #Subtraction
25
# multiplication
3*4
12
# division
60 / 2
30.0
# power operation
2 ** 3
8
(5 + 4) * (20 -5)
135
# Expression
18
18
x = 0
x + 18
18
x + 20
20
# Order Of Operations Using PEMDAS Rule
#Parantheses
2 * (4 -2)
4
(2 + 3) * 4
20
# Exponentiation
2 ** 1 + 3
5
3*1**3
3
# Multiplication and Division
# Addition and Subtraction
2 * 3 - 1
5
6 + 4 / 2
8.0
# operators with same precedence from left to right
5 - 3 - 1
1
6 + 3 - 1 + 4 + 5 * 4 + 3 * 4 / 2
38.0
# Modulus Operator
7 / 3
2.3333333333333335
7 % 3
1
7 // 3
2
# String Operation With + operator
first = '10'
second = '15'
first + second
'1015'
# * Operator
x = 'Test'
y = 3
x * y
'TestTestTest'
x = 'Test '
x * 3
'Test Test Test '
# How To Ask Data From The User?
x = input()
7
y = input("Enter The Y value > 0:" )
Enter The Y value > 0:2
x + y
'72'
x = int(x)
y = int(y)
x + y
9
y = int(input("Enter The Y value > 0:" ))
Enter The Y value > 0:3
type(y)
<class 'int'>
# \n
y = int(input("Enter The Y value > 0:\n " ))
Enter The Y value > 0:
 7
type(y)
<class 'int'>
y = int(input("Enter The Y value > 0:\n" ))
Enter The Y value > 0:
"I am Pruthvi"
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    y = int(input("Enter The Y value > 0:\n" ))
ValueError: invalid literal for int() with base 10: '"I am Pruthvi"'
# How To Write comments
minute = 200
percentage = (minute * 100) / 60
percentage = (minute * 100) / 60  # Compute percentage
v = 5 # Assign 5 to v
v = 5 # Velocity in m/sec
# mnemonic variables
hours = 24
rate = 23
pay = hours*rate
