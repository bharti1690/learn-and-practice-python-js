# Slicing - return a subset of the list. You specify the start index and the end index, separated by a colon, to return a part of the list.
b = "Hello, World!"
print(b[2:5]) # Get the characters from position 2 to position 5 (not included)

#Slice from the start
print(b[:5])
#Slice from the end
print(b[2:])

#Negative indexing
# Use negative indexes to start the slice from the end of the string
# Example: Get the characters: From: "o" in "World!" (position -5) To, but not included: "d" in "World!" (position -2):
print(b[-5:-2]) 

#lower() method returns the string in lower case
#upper() method returns the string in upper case
print(b.lower())
print(b.upper())

#strip() method removes any whitespace from the beginning or the end
print(b.strip())

#replace() method replaces a string with another string
print(b.replace("H", "J"))

#split() method splits the string into substrings if it finds instances of the separator
print(b.split(","))

#Concatenate two strings
a = "Hello"
b = "World"
c = a + b
print(c)

#f-string is a way to format strings in Python
age=34
txt = "My name is John, and I am {age}"
print(txt.format(age=age)) # Output: My name is John, and I am 34
print(txt)  # Output: My name is John, and I am {age} because the variable age is not defined
txt = f"My name is John, and I am {age}"
print(txt)  # Output: My name is John, and I am 34 because the variable age is defined. f is used to format the string

# escape characters "/" is used to insert characters that are illegal in a string

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# \n is used to insert a new line. there are several escape characters in Python. Refer to w3schools.com for more information.
#string methods are used to manipulate strings. Refer to w3schools.com for more information.

#bool() method is used to evaluate a value and return True or False
print(bool("Hello"))
print(bool(15)) 
#__len__() method returns the length of the string
class myclass:
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

#isinstance() method is used to check if an object is an instance of a class
x = 100
print(isinstance(x, int))
#Arithmetic operators are used with numeric values to perform common mathematical operations (+, -, *, /, %, **, //)