import sys

print(sys.version) # To check the version of Python you are using, you can use the sys module

print('Hello World!') # To print a string in Python, you can use single quotes or double quotes

if 5> 2:
    print('Five is greater than two!')  # Indentation is important in Python and is used to define a block of code

# Comments in Python start with the hash character, #, and extend to the end of the physical line

# Variables in Python are created when you assign a value to it
x= 5 
y= 'Hello, World!'
print(x)
print(y)  # Variables do not need to be declared with any particular type, and can even change type after they have been set.

z = 4       # x is of type int
z = "Sally" # x is now of type str
print(z)

# Python has two primitive number types: int and float. 
# Casting is used to specify a type on a variable
# Variable names are case-sensitive.

i = int(3)
j = float(3.0)
k = str(3)

I = 3

# You can get the data type of a variable with the type() function
print(type(i))

# Unpack a collection of values into variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)

# Assign the same value to multiple variables in one line
x = y = z = "Orange"

# Output variables using the print() function
print("I like " + x + ", " + y + ", and " + z + " juice.")
x=20
y=50
print(x+y) # Python uses the + operator to add numbers, and the + operator to concatenate strings

# Global variables can be used by everyone, both inside of functions and outside
x = "Wonderful"

def myfunc():
    x = "Fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)

# To create a global variable inside a function, you can use the global keyword.
def myfunc():
    global x 
    x = "Awesome"

myfunc()
print("Python is " + x)

# Type conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random number
import random
print(random.randrange(1, 10)) # The randrange() method returns a randomly selected element from the specified range