# Python Input and Output

# Python Output

# We use the print() function to output data to the standard output device

print("hello world")

a = 20

print("the value of a is", a) # 20
print("the value of a is " + str(a)) # the value of a is 20

# Output Formatting

a = 10; b = 20 # multiple statements in single line.

print("the value of a is {} and b is {}".format(a,b)) # the value of a is 10 and b is 20
# string has format() function

a = 10; b = 20

print("the value of b is {1} and a is {0}".format(a,b)) #  specify position
# the value of b is 20 and a is 10


# we can use keyword arguments to format the string

print("hello {name}, {greeting}".format(name = "mihir", greeting = "Good Morning"))
# hello mihir, Good Morning

# we can combine positional arguments with keyword arguments

print('the story of {0}, {1} and {other}'.format('Bill','Manfred',other="Georg"))
# the story of Bill, Manfred and Georg

#--------------------------------------***--------------------------------------------------------------------------

# Python Input

# Want to take the input from the user. In python, we have the input() function to allow this.

num = int(input("Enter a Number: "))
print(num)
print(type(num))