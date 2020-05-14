# Name: ...
# CSE 160
# Spring 2018
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and then copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all of the problems given.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print("Problem 1 solution follows:")

#quadratic equation = 3 x**2 -5.86x + 2.5408
# solution 1: (-b + sqrt(b^2 - 4ac))/2a and solution 2: (-b - sqrt(b^2 - 4ac))/2
# with a = 3, b = -5.86 and c = 2.5408

# Computes the roots of the quadratic equation written above 
x_1 = ( 5.86 - math.sqrt((-5.86)**2 - 4*3*2.5408) ) / (2*3)
x_2 = ( 5.86 + math.sqrt((-5.86)**2 - 4*3*2.5408) ) / (2*3)

# Prints the roots
print('The roots of the quadratic equation, with the smaller root first, are {} and {}'.format(x_1, x_2), '\n')

###
### Problem 2
###

print("Problem 2 solution follows:")

# Prints the decimal representations of 1/2, 1/3, ..., 1/10
for i in range(2, 11):
    print(1/i, '\n')



###
### Problem 3
###

print("Problem 3 solution follows:")

# Computes the 1Oth triangular number

# Initial value of triangular_10
triangular_n = 0

# Sets the number n
# We want the 10th triangular so n = 10
n = 10

# Computes triangular_n using a for loop
for i in range(1, n + 1):
    
    triangular_n += i

print('The 10th triangular number is {}.'.format(triangular_n), '\n')
    

###
### Problem 4
###

print("Problem 4 solution follows:")

# Initial value of factorial
factorial_n = 1

# Sets the number n
# We want the factorial of 10 so n = 10
n = 10

# Computes factorial_n using a for loop
for i in range(1, n + 1):
    
    factorial_n *= i

print('The factorial of 10, 10!, is equal to {}.'.format(factorial_n), '\n')

###
### Problem 5
###

print("Problem 5 solution follows:")

numlines = 10

for n in reversed(range(numlines + 1)):
    
    factorial = math.factorial(n)
    
    print(factorial, '\n')
    
    
###
### Problem 6
###

print("Problem 6 solution follows:")

result = 0

n = 10 

for n in range(n + 1):
    result += 1/math.factorial(n)
        
      
print('The value sought is equal to {}.'.format(result))
    

###
### Collaboration
###

# No one


