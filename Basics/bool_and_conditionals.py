#Boolean data types and conditionals
door_is_locked = False
if door_is_locked: 
    print("Open the door!")
else: 
    print("Let's go inside")

#Comparison operators are all the same as JS
print(5>3)
print(3>5)
print(10>=10)
print(10<=9)
print('a' == 'a')
print('a' != 'b')

#logical operators
print(True and True)
print(True or False)
print(not False)

#strangely, you can do math with true and false in python
#normally, you can't add a string to a number or other data types
# print('pop' + 1) #this causes an error
#but true and false evaluate to 1 and 0
print(True + 3)
print(False + 3)