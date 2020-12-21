import os

left_int = int(input('Enter left side number of equal sign> '))
operator = input('Enter operator(+, -, *, /)> ')
right_int = int(input('Enter right side number of equal sign> '))

def addition():
	print(left_int + right_int)

def subtraction():
	print(left_int - right_int)

def multiplication():
	print(left_int * right_int)

def division():
	print(left_int / right_int)

if operator == '=':
	addition()

elif operator == '-':
	subtraction()

elif operator == '*':
	multiplication()

elif operator == '/':
	division()

else:
    print('Something went wrong... Try again.')
	
os.system('pause')
