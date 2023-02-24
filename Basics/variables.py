#Variable declaration
name = "stranger" #declares variable name with str value stranger

print("Hello", name) #logs Hello stranger ot the console

#example of a function containing a conditional
def bigger_than_five(x):
    if x>5:
        print("x is bigger than five")
    else:
        print("x is 5 or smaller")

bigger_than_five(10)
bigger_than_five(2)

#like JS, Python does not declare data type
my_name = "Natalie"
my_age = 29
my_salary = 80217

#when naming variables, follow_underscore_convention_like_in_R
# ...camelCase is reserved for class names
#to know the data type, use type()
print(type(my_name))
print(type(my_age))
