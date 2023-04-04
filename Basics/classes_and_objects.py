# objects encapsulate variables and functions into a single entity
# classes are templates to create objects

#this class contains a variable and a function
class MyClass:
    variable = 'meh'

    def function(self):
        print('This is a message inside a class.')

#this is an object made from MyClass
myobjectx = MyClass()

#it has the same properties as MyClass
print(myobjectx.variable) #this prints 'meh'
myobjectx.function()


# multiple objects can be of the same class, but the copies of
# class variables are independent, and changing them in one object
# does not affect the others
myobjecty = MyClass()

myobjecty.variable = 'whoops'

print(myobjecty.variable) #this is whoops instead of meh

# when initiating a class, you can also you _init_() function,
# which is used to assign values in a class
class NumberHolder:

    def __init__(self, number):
        self.number = number

# object/class exercise
# define a Vehicle class
class Vehicle: 
    name = ''
    kind = 'car'
    color = ''
    value = 100.00
    def description(self):
        desc_str = f'{self.name} is a {self.color} {self.kind} worth {self.value}'
        return desc_str
    
#make one car a red convertible worth $60,000.00 with a name of Ferrari
car1 = Vehicle()
car1.name = 'Ferrari'
car1.color = 'red'
car1.kind = 'convertible'
car1.value = 60000.00

# make a second car that is a blue van named Jump worth $10,000.00
car2 = Vehicle()
car2.name = 'Jump'
car2.color = 'blue'
car2.kind = 'van'
car2.value = 10000.00

#call description on both cars
print(car1.description())
print(car2.description())