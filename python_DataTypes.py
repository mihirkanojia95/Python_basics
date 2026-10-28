# Data Types in Python

'''
Every value in Python has a datatype. Since everything is an object in Python programming, data
typws are actually classes and variables are instance (object) of these classes.

'''

# Numbers

'''
integers, floating point numbers and complex numbers falls under Python numbers category.
they are defined as int, float and complex classes in Python.

we can use the type() function to know which class a variable or a value belongs to and the isinstance()
function to check if an object belongs to a particular class.

'''

a = 5 # data type is implicitly set to integer
print(a, "is of type", type(a))

a = 2.5 # data type is changed to float
print(a, "is of type", type(a))

a = 1 + 2j # data type is changed to complex number
print(a,"is complex number?")
print(isinstance(1 + 2j, complex))
print(type(a))


# Boolean

# Boolean represents the truth values False and True.

a = True
print(type(a))

a = False
print(type(a))


# Python Strings

'''
String is a sequence of Unicode characters. (it can stored non-english characters as well).

We can use Single quotes or double quotes to represent strings.

Multi-line strings can be denoted using triple quotes,

A string in Python consists of a series or sequence of characters - letters, numbers, and special characters.

Strings can be indexed - often synonymously called subscripted as well.

Similar to C, the first character of a string has the index 0.

'''


s = "this is Online AI Course" # oR 'this is online AI Course' single quotes
print(s)
print(type(s)) # <class 'str'>
print(s[0]) # t ,first character of the string

# print the last character of the string
print(s[-1]) # e, last character of the string
print(s[len(s)-1]) # e, last character of the string

# String Slicing
print(s[5:]) # 5 to end index characters
print(s[5:10]) # 5 to 9 index characters, [5,10) 10 is not included
print(s[:10]) # 0 to 9 index characters, [0,10)


# Multi-line String

s = """ this is a multi-line string
         and AI is the future of technology """
print(s)
print(type(s)) # <class 'str'>

# String Slicing
print(s[5:]) # 5 to end index characters
print(s[5:10]) # 5 to 9 index characters, [5,10) 10 is not included
print(s[:10]) # 0 to 9 index characters, [0,10)


# Python List (actually a dynamic array)

'''
List is an ordered sequence of items. it is one of the most used datatype in 
Python and is very flexible. All the items in a list do not need to be of the 
same type.

Declaring a list is, Items separated by commas and enclosed within square 
brackets [].

'''

a = [10, 20.5, "hello"] 

print(a) # [10, 20.5, 'hello'], print the whole list

print(a[1]) # 20.5, print 1st index element of the list
print(a[2]) # hello, print 2nd index element of the list

# Lists are mutable, meaning, the value of elements of a list can be altered.

a[0] = 100
print(a) # [100, 20.5, 'hello'], first element of the list is changed to 100 from 10


# Python Tuple

'''
Tuple is an ordered sequence of items same as list. the only differnce is that is 
that tuples are immutable. tuples once created cannot be modified. 
Tuples are defined using parentheses ().

'''

t = (1, 2.5, "ML") # tuple with mixed datatypes
print(t) # (1, 2.5, 'ML'), print the whole tuple
print(t[1]) # 2.5, print 1st index element of the

# TypeError: 'tuple' object does not support item assignment
# t[1] = 3.4, tuples are immutable
# print(t)


# Python Set

'''
Set is an unorderd collection of unique items. Set is defined by values 
separated by comma inside braces {}. Items in a set are not ordered.

Set have unique values.

'''
a = {10, 30, 20, 40, 5}
print(a) # {20, 5, 40, 10, 30}
print(type(a)) # <class 'set'>

# We can perform Set Operations like union, intersection on two sets.
# Set have unique values.

s = {10, 20, 20, 30, 30, 30}

print(s) # {10, 20, 30}, automatically set won't consider duplicate elements

# TypeError: 'set' object is not subscriptable
# print(s[1]) # we can't print particular element in set because it's unorder collections of items


# Python Dictionary (think like hash-table)

'''
Dictionary is an unorderd collection of key-value pairs.

In Python, dictionaries are defined within braces {} with each item being a pair 
in the form key:value.

key and value can be of any type.

'''

d = {
    'a': "apple",
    'b': "bat"
}

print(d)
print(type(d)) # <class 'dict'>

print(d['a']) # apple, you can use the key to access the specific row in a table
print(d['b']) # bat
# print(d['c']) # KeyError: 'c'

#-------------------------------------------------***--------------------------------------

# Conversion B/w Datatypes

'''
We can convert b/w different data types by using different type conversion functions
like int(), float(), str() etc.  

'''

# Convert integer to float using float() method
a = 4
print(float(a)) # 5.0

# Convert float to integer using int() method
print(int(100.5)) # 100


# Convert integer to string using str() method
print(str(20)) # '20'

# Conversion to and from string must contain compatible values.

# print(int('10p')) # ValueError: invalid literal for int() with base 10: '10p'

print(int('10')) # 10

user = "mihir"
lines = 100

print("Congratulations, " + user + "! You just wrote " + str(lines) + " lines of code ")


#-------------------------------------------***----------------------------------------

# We can convert one sequence to other

a = [1, 2, 3]
print(type(a)) # type of a is list

s = set(a) # convert list to set using set() method

print(type(s)) # now type of s is set

# convert String to list using list() method

print(list("hello")) # ['h', 'e', 'l', 'l', 'o']






