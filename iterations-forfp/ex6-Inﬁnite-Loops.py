# Inﬁnite Loops

# Example for infinite loop.
i = 1
while True:
    print(i)
    # Do something forever. .
#%%
# Program to find the factors of the number
# List the factors of the integers 1...MAX
MAX = 20                            # MAX is 20
n = 1                               # Start with 1
while n <= MAX:                     # Do not go past MAX
    factor = 1                      # 1 is a factor of any integer
    print(end=str(n) + ': ')        # Which integer are we examining?
    while factor <= n:              # Factors are <= the number
        if n % factor == 0:         # Test to see if factor is a factor of n
            print(factor, end=' ')  # If so, display it
            factor += 1             # Try the next number
    print()                         # Move to next line for next n
    n += 1
#%%
MAX = 20                            # MAX is 20
n = 1                               # Start with 1
while n <= MAX:                     # Do not go past MAX
    factor = 1                      # 1 is a factor of any integer
    print(end=str(n) + ': ')        # Which integer are we examining?
    while factor <= n:              # Factors are <= the number
        if n % factor == 0:         # Test to see if factor is a factor of n
            print(factor, end=' ')  # If so, display it
        factor += 1             # Try the next number
    print()                         # Move to next line for next n
    n += 1

#%%
# Nested for loop to find the factors instead of nested while loops

# List the factors of the integers 1...MAX
MAX = 20                                # MAX is 20
for n in range(1, MAX + 1):             # Consider numbers 1...MAX
    print(end=str(n) + ': ')            # Which integer are we examining?
    for factor in range(1, n + 1):      # Try factors 1...n
        if n % factor == 0:             # Test to see if factor is a factor of n
            print(factor, end=' ')      # If so, display it
    print()                             # Move to next line for next n
#%%

