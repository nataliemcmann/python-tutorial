#functions are defined by the block keyword "def"
def my_function():
    print("Hello from a function!")

#use the parentheses to pass in arguments
def my_function_with_args(username, greeting):
    print(f'Hello, {username}, I wish you {greeting}')

#use return to return a value
def sum_two_numbers(a, b):
    return a+b

#to call functions, simply write their name
my_function()
my_function_with_args('Natalie', 'a happy day!')
x = sum_two_numbers(2, 2)

#function building exercise
# list_benefits should return a predetermined list of strings
def list_benefits():
    return [
        'More organized code', 
        'More readable code', 
        'Easier code reuse',
        'Allowing programmers to share and connect code together'
        ]

# build_sentence should receive a single string argument 
# and return a sentence that starts with the given string and ends
# with "...is a benefit of functions!"
def build_sentence(benefit):
    return f'{benefit} is a benefit of functions!'

# name_benefits_of_functions should combine the previous functions to
# print out sentences about the benefits of functions
def name_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

#call function from line 36 to see results
name_benefits_of_functions()