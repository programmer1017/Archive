import random
import os
import time

print("Making passwords...")
time.sleep(1)

min_int = int(input("Minimum number of integer..."))
max_int = int(input("Maximum number of integer..."))
min_str = int(input("Minimum number of string..."))
max_str = int(input("Maximum number of string..."))
min_uni = int(input("Minimum number of special charicters..."))
max_uni = int(input("Maximum number of special charicters..."))
print('Your safe password is: ')

a = random.randint(min_int, max_int)
b = random.randint(min_str, max_str)
c = random.randint(min_uni, max_uni)
list_of_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

list_of_alphabets = ['q', 'w', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z','x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

list_of_unique_charaters = ['!', '?', '^', '<','>', '@', '#', '$', '%', '*', '(', ')', '-', '+']

pwd_abc = []
pwd_123 = []
pwd_unique = []


def check():
    retry = str(input('Try again? (y/n)> '))
    if retry == 'y':
        generate_password()
    if retry == 'n':
        print('See you again!')
        os.system('pause')
    else:
        print('Something went wrong... Try again.')
        check()

def generate_password():
    global a, b, c
    for cat in range(a):
        added_list_of_numbers = random.choice(list_of_numbers)
        pwd_123.append(added_list_of_numbers)
    
    for dog in range(b):
        added_list_of_alphabets = random.choice(list_of_alphabets)
        pwd_abc.append(added_list_of_alphabets)
    
    for bird in range(c):
        added_unique = random.choice(list_of_unique_charaters)
        pwd_unique.append(added_unique)


    final_list = pwd_unique + pwd_abc + pwd_123
    random.shuffle(final_list)
    len_final = len(final_list)
    mouse = 0
    print_pwd = ""
    for iphone in range(len_final):
        print_pwd = print_pwd + final_list[mouse]
        mouse = mouse + 1
    print(print_pwd)
    check()


generate_password()
