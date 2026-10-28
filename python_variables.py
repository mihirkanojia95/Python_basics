# Variables

'''
A variable is a location in memory used to store some data (value).

they are given unique names to differentate b/w different memory locations. the rules
for writing a variable name is same as the rules for writing identifiers in python.

we don't need to declare a variable before using it. In python; we simply assign a value to a variable
and it will exist. We don't even have to declare the type of the variable. this
is handled internally according to the tupe of value we assign to the variable.

'''

# Variable Assignments

# we use the assignment operator (=) to assign a value to a variable.

a = 10. # integer
b = 5.5 # float
c  = "ML" # string (two characters in double quotes)

# Multiple Assignments

a,b,c = 10, 5.5, "ML" # multiple assignment in a single line

a = b = c = "AI" # assign the same value to multiple variables at once

#-----------------------------------------------***----------------------------------------------------


# Storage Location

x = 3 
print(x) # 3
print(id(x)) # print address of variable x 4358336544

x = 3 # now change the value 3 to 5
print(x) # 5
print(id(x)) # 4358336608

y = 3
print(id(y)) # print address of variable y

# observation: both x and y have the same value, so they are stored in the same memory location. hence, they have the same address.

y = 4
print(id(y)) # print address of variable y



