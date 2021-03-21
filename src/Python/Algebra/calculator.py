import os

left_int = int(input('Enter left side number of equal sign> '))
operator = input('Enter operator(+, -, *, /)> ')
right_int = int(input('Enter right side number of equal sign> '))


def before_answer():
    print("The answer is: ")
    print()


def addition():
    before_answer()
    print(left_int + right_int)


def subtraction():
    before_answer()
    print(left_int - right_int)


def multiplication():
    before_answer()
    print(left_int * right_int)


def division():
    before_answer()
    print(left_int / right_int)


# end of defining functions...
if operator == '-':
    subtraction()

elif operator == '*':
    multiplication()

elif operator == '/':
    division()

elif operator == '+':
    addition()

else:
    print('Something went wrong... Try again.')

os.system('pause')
