#python strings

#like JS, Python is loosely typed and does not declare data type
my_name = "Natalie"
my_age = 29
my_salary = 80217

# declared with quotes (either single or double, use double to use apostrophes)
#python does prefer single quotes, just like JS
# operators work on them (addition and multiplication specifically)

print('a' + 'b')
print('ab' * 3)
print("She's a brickhouse.")
#backslash also works
print('She\'s mighty mighty.')

#there's also """ triple quotes, which allow for multiline strings and escaping quotations"""
print(""" If I knew any
...song lyrics""")
#but also there's a syntax to make new lines (this is used in R as well)
# \n makes a new line
# \r carriage return (google that)
# \t tab
# \\ gives you a \ character instead of causing an escape
print('If I knew any \n...song lyrics')

#string operations: like JS methods, you can call functions on variables in python
mystring = 'string'
print(mystring.capitalize())
print(mystring.upper())
print(mystring.lower())
#more operations and their documentation can be found in the Python documentation

#get string length with len() function
print(len(mystring))

#split a string into an array with .split()
hello = 'Hello, world'
print(hello.split(',')) #calling .split() with no argument will split on whitespace

#replace parts of a string
print(hello.replace('H', 'h'))

#f-strings (or template literals)
print(f'My name is {my_name}')
#f-strings can also be used to console log variables
print(f"{my_age=}, {my_name=}" )