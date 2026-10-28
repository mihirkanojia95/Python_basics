# Python Statement

# instructions that a python interpreter can execute are called statements.

# Example

a = 1   # single-line statement
print(a)

# multi-line statement

# in Python, end of a statement is marked by a newline character. but we can make a statement extend over multiple lines with the line continuation character ().

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

print(a)


# anthoer way is to use parentheses, brackets or braces to enclose the statement. in this case, we do not need to use the line continuation character.
a = (1 + 2 + 3 +
     4 + 5 + 6 +
     7 + 8)

print(a)

# put multiple statements in a single line using ;

a = 1; b = 2; c = 3
print(a,b,c)