# to get python working:
# run python3 -m venv env
# source ./env/bin/activate
# pip3 install package_name

#once python is successfully set up, you can hit the play button in the top right corner of VSCode
#to run the code in the terminal
# name = "stranger" #declares variable name with str value stranger

# print("Hello", name) #logs Hello stranger ot the console

#example of a function containing a conditional
# def bigger_than_five(x):
#     if x>5:
#         print("x is bigger than five")
#     else:
#         print("x is 5 or smaller")

# bigger_than_five(10)
# bigger_than_five(2)

#like JS, Python does not declare data type
my_name = "Natalie"
my_age = 29
my_salary = 80217

#operators
# print(2+2) #addition
# print(2-2) #subtraction
# print(5*5) #multiplication
# print(30/6) #division
# print(20%2) #modulus or remainder?
# print(11%2) #def remainder
# print(300//3) #floor division
# print(4**2) #exponent 

#pretty straightforward so far

#variable and expression
# result = 3 * 5
# print(result - 4)

#when naming variables, follow_underscore_convention_like_in_R
# ...camelCase is reserved for class names
#to know the data type, use type()
# print(type(my_name))
# print(type(result))

#python strings
# declared with quotes (either single or double, use double to use apostrophes)
#python does prefer single quotes, just like JS
# operators work on them (addition and multiplication specifically)

# print('a' + 'b')
# print('ab' * 3)
# print("She's a brickhouse.")
# #backslash also works
# print('She\'s mighty mighty.')

#there's also """ triple quotes, which allow for multiline strings and escaping quotations"""
# print(""" If I knew any
# ...song lyrics""")
#but also there's a syntax to make new lines (this is used in R as well)
#\n makes a new line
#\r carriage return (google that)
#\t tab
#\\ gives you a \ character instead of causing an escape
# print('If I knew any \n...song lyrics')

#string operations: like JS methods, you can call functions on variables in python
# mystring = 'string'
# print(mystring.capitalize())
# print(mystring.upper())
# print(mystring.lower())
#more operations and their documentation can be found in the Python documentation

#get string length with len() function
# print(len(mystring))

#split a string into an array with .split()
hello = 'Hello, world'
print(hello.split(',')) #calling .split() with no argument will split on whitespace

#replace parts of a string
# print(hello.replace('H', 'h'))

#f-strings (or template literals)
# print(f'My name is {my_name}')
#f-strings can also be used to console log variables
# print(f"{my_age=}, {my_name=}" )

#Boolean data types and conditionals
door_is_locked = False
if door_is_locked: 
    print("Open the door!")
else: 
    print("Let's go inside")

#Comparison operators are all the same as JS
# print(5>3)
# print(3>5)
# print(10>=10)
# print(10<=9)
# print('a' == 'a')
# print('a' != 'b')

#logical operators
print(True and True)
print(True or False)
print(not False)
