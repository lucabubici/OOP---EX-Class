# APPEND
# def add_snack(grocery_list): 
#     grocery_list.append("Tim Tams") # Modifies the opriginal list
#     grocery_list.append("Kinder Bueno")
# my_bag = ["Milk", "Bread"]

# add_snack(my_bag)

# print(my_bag) # Tim Tams are now in the bag

# REPLACE
# def update_first_item(x):
#     x[1] = "Vegemite"

# breakfast = ["Jam", "Butter", "Toast"]

# update_first_item(breakfast)

# print(breakfast)

# BROKEN LINKS
# def change_list(x):
#     x = ["Banana", "Apple", "Orange"] # the link is broken here IN PYTHOH THIS IS CALLED 'BROKEN LINK'

# original_list = ["Plum", "Orange"]

# change_list(original_list)
# print(original_list) # still prints ['Plum', 'Orange']

# def myFun(x):
#     x = 20 # breaks the link
# x = 10
# myFun(x)
# print(x) # output is still 10

# def printMe(str):
#     print(str)

# printMe("Hello")

# def printInfo(name, age):
#     print(f"Name: {name}, Age: {age}")

# printInfo(age = 50, name = "Toyen")

# def printInfo(name, age=26): # 35 is by default
#     print(f"Name: {name}, Age: {age}")

# printInfo("Laura")

# def invite_guests(*guests):
#     print(f"Guests arriving: {guests}")

# invite_guests("Alice", "Bob")

# def printInfo(arg1, *vartuple):
#     print(f"First: {arg1}")
#     for var in vartuple:
#         print(f"Extra: {var}")

# printInfo(10,70,60,50)

# # Lambda
# my_sum = lambda arg1, arg2: arg1 + arg2

# print(f"Lambda total: {my_sum(10,20)}")

total = 0 # Global

# def sum_nums(arg1, arg2):
#     total = arg1 + arg2
#     print(f"Inside local total: {total}")

# sum_nums(10,20)
# print(f"Outside global total: {total}")

def calculate(num1,num2):
    return num1 + num2, num1 - num2

add, sub = calculate (10,20)
print(f"Addition: {add}. Subtraction: {sub}")

