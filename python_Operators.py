# Operators

'''
Operators are special symbols in python that carry out arithmetic or logical 
computation. the value that the operator operates on is called the operand.

Operator Types

1. Arithmatic operators
2. Comparison (Relational) operators
3. Logical (Boolean) operators
4. Bitwise operators
4. Assignment operators
5. Special operators

'''
# Arithmetic Operators

'''
Arithmetic operators are used to perform mathematical operations like addition, 
subtraction, multiplication etc.

+ , -, *, /, %, //, ** are arithmetic operators

'''

# Example

x , y = 10, 20

print(x,y) # x = 10, y = 20

print(x + y) # addition
print(x - y) # Subtraction
print(x*y) # multiplication
print(x/y) # division --> return a float value
print(x%y) # modulo division --> gives remainder
print(x // y) # floor Division
print(x ** y) # Exponent --> (10^20)

print(-15 // 2) # -8
print(2 ** 5) # 2^5 = 32

#-------------------------------------------***----------------------------------------------------------------------------------------------------------------------------------

# Comparison Operators

'''
Comparison operators are used to compare the values. it either returns True of False
according to the condition.

 >, <, ==, !=, >=, <= are comparision operators

'''

a, b = 10, 20

print(a,b) # a = 10, b = 20

# check a is less than b (strictly less than)
print(a < b)

# check a is equal to b
print(a == b)

# check a is greater than b (strictly greater than)
print(a > b)

# check a is not equal to b (!=)
print(a!=b)

# check a is greater than or equal to b
print(a >= b)

# check a is less than  or equal to b
print(a <= b)

#---------------------------------------------***------------------------------------------------------------------------------------------

# Logical Operators

# Logical operators are and, or, not operators.it return True or False

a, b = True, False

print(a,b) # a = True, b = False

# print a and b
print(a and b) # False

# print a or b
print(a or b) # True

# print not a
print(not a) # False

# print not b
print (not b) # True

#-----------------------------------------***-----------------------------------------------------------

# Bitwise Operators

'''
Bitwise operators act on operands as if they were string of binary digits.
it operates bit by bit

&, |, ~, ^, >>, << are bitwise operators

'''
a, b = 10, 4

print(a,b) # a = 10, b = 4

# Bitwise AND
print( a & b) # 0

# Bitwise OR
print( a | b) # 14

# Bitwise NOT
print(~a) # -11

# Bitwise XOR
print(a ^ b) #14

# Bitwise left-shift
print(a<<b) # 160

# Bitwise Right-shift
print(a >> b) # 0

#------------------------------------------------***-----------------------------------------------------------------------

# Assignment Operators

'''
Assignment operators are used in python to assign values to variables.

a = 5 is a simple assignment operator that assigns the value 5 on the right to the
variable a on the left.

  =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<= are Assignment operators

'''
a = 10
print(a) # a = 10

a += 20
print(a) # a = 30

a -= 20
print(a) # a = 10

a *= 20
print(a) # a = 200

a /= 20
print(a) # a = 10.0

a %= 20
print(a) # 10.0

a //= 20
print(a) # 0.0

a **= 20
print(a) # 0.0

#------------------------------------------****-----------------------------------------------------------------------------------------

# Special Operators

# Identity Operators

'''
is and is not are the identity operators in python.

they are used to check if two values (or variables) 
are located on the same part of the memory.

The is operator returns True if both variables refer to the same object.

The is not operator returns True if two variables refer to different objects.

'''
a = 5
b = 5
print(id(a)) # 4402278496
print(id(b)) # 4402278496

print(a is b) # 5 is object created once both a and b points to same object
# True

a = [10, 20, 30]
print(id(a)) # 4378761472
b = a
print(id(b)) # 4378761472

print(a is b) # true



l1 = [1, 2, 3]
l2 = [1, 2, 3]

print(id(l1)) # 4368341248
print(id(l2)) # 4368518464

print(l1 is l2) # False

s1 = "AAIC"
s2 = "AAIC"

print(id(s1)) # 4373488160
print(id(s2)) # 4373488160

print(s1 is s2) # True

#--------------------------------------------***-------------------------------------------------------------------------------------

# MemberShip Operators

'''
in and not in are the membership operators in Python.

they are used to test whether a value or variable is found in a sequence (String, list,
tuple, set and dictionary).

'''

lst = [1, 2, 3, 4]

# check 1 is present in a given list or not
print(1 in lst) # True

# check 5 is present in given list
print(5 in lst) # False


# this is a dictionary
d = {
    1: "a",
    2: "b"
}

# only check the keys not values
print(1 in d) # True
print(2 in d) # True
print(3 in d) # False











