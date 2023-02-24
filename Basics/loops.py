#there's two ways to loop

#good ol' for loop
for letter in 'Hello':
    print(letter)

#general template is 
# for <variable> in <iterable>:
#   do something

#loops let us do things with secondary data structures
#like in c#, lists are more useful than arrays in Python
my_list = ['a', 1, 'Hello'] #lists can hold many data types
#arrays require an import module
from array import *
my_array = array('i', [10, 20, 30, 40, 50]) #the import array lets us set the 
#typecode, or data type, of the data in the array
#both lists and arrays are iterable

for item in my_list:
    print(item)

for item in my_array:
    print(item)

#list can be nested, but not arrays
my_nestedlist = [1, 2, [3, 8], 3]
print(my_nestedlist[2]) #called indices is much the same as JS
for item in my_nestedlist:
    print(item)

#good ol' while loop
# while <expression evaluates to True>:
#   do the thing
i = 1 #start with i = 1
#loop to count 1-4
while i <= 4: 
    print(i) 
    i = i + 1 #increment i

#infinite loops...sometimes, you don't want it to stop.
#if your expression evaluates alway to true, like while True, for example
#then the loop will continue until you ctrl c the terminal

#skipping to list comprehensions or....python version of js methods like .map, .filter
#list comprehensions create lists from existing lists
# general syntax: 
# [ <expression> for item in list <conditional or function to apply to list> ]

#map range for a list
print([x for x in range(1, 6)]) #gives [1, 2, 3, 4, 5]
# can also do 
print(list(range(1,6)))
#filter range for a list of even numbers
print([x for x in range(1,10) if x % 2 == 0]) # gives [2, 4, 6, 8]

#expressions can be anything that is valid code
print([x + 4 for x in [10, 20]]) #gives [14, 24]

#it is likely most common for a function to be in expression
def some_function(a):
    return (a + 5) / 2

m = [some_function(x) for x in range(8)] #applies function to numbers 1-8
print(m)