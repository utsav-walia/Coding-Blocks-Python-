# Part 1

print("Hello", end=",")
print("World")

print("Hello","World",sep="\n")

# Input
a = 1
b = 6
print(a+b)

# Part 2

"""
Data Types:

Numeric type - int, float, complex
Text type - str

Sequence type - list, tuple, range
Mapping type - dict
Set type - set
Boolean type - bool

Basic data types -> int, float, complex, str, bool
Advanced data types -> list, tuples, dict, set

"""

# Type casting methods int, float, complex
ab = float(input("Enter float: "))
print(ab)

# Part 3

"""Operators 
1. Arithmetic operators -> +,-,*,/,**,//,%
"""
c = int(input("Enter c: "))
d = int(input("Enter d: "))

print("{x} + {y} = {z}".format(x=c, y=d, z=c+d))
print("{x} * {y} = {z}".format(x=c, y=d, z=c*d))
print("{x} / {y} = {z}".format(x=c, y=d, z=c/d))
print("{x} - {y} = {z}".format(x=c, y=d, z=c-d))
print("{x} ** {y} = {z}".format(x=c, y=d, z=c**d))
print("{x} // {y} = {z}".format(x=c, y=d, z=c//d))
print("{x} % {y} = {z}".format(x=c, y=d, z=c%d))

# Operator Pecedence BODMAS
# Modulus is greater than BODMAS






