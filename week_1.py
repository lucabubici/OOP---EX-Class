my_car = "Toyota"
fuel_level = 100

# f is an instruction to ask the machine to fill the gap (curly braces) with the value in those variables
print(f"The name of my car is {my_car} and I have {fuel_level} %")


# TYPES OF VARIABLES
no_of_pies = 5
price_of_a_pie = 4.5
total_checkout = {no_of_pies * price_of_a_pie}
print(f"Total checkout is total_checkout")


# COLLECTION type -> LIST
grocery_list = ["milk","bread","butter","chicken", "chicken"]
print(f"grocery list: {grocery_list}")
print({grocery_list[-5]})

# COLLECTION type -> SET
# grocery_set = {"milk", "bread", "butter", "chicken", "chicken"}
# print({grocery_set})


# COLLECTION type -> DICTIONARY
slang = {"arvo":"afternoon", "barbie":"BBQ", "bikkie":"biscuit"}
print(f"Arvo is :{slang['arvo']}")

# INDENTATION EXAMPLE: HOW LOGICS/STATEMENTS WORK
if True:
    print(f"I am indented. I am part of this IF family")
print(f"This is not anymore part of the previews IF family. Because this is not indented, so not considered part of previews IF")

# POWER OF (OPERATIONS)
bank_balance = 10
bank_balance **= 2
print({bank_balance})

# INCREMENT ASSIGNMENT +=
score = 50
score += 10 # This is the same as: score + 10
print({score})

# SUBTRACTION ASSIGNMENT -=
wallet = 100
wallet -= 5.50 # This is the same as: wallet - 5.50
print({wallet})

# MULTIPLICATION AISSGNMENT *=
bet = 20
bet*= 2 # This is the same as: bet = b et * 2
print({bet})

# DIVISION ASSIGNMENT /=
total_slices = 12
friends = 4
total_slices /= friends # This is the same as: total_slices = total_slices /friends
print({total_slices})

# BASIC CONDITION TEST -> IN
maccas_menu = ["Nuggets", 'Big Mac', "Fried"]
print({f'Big Tasty' in maccas_menu})

print("Help"[2:4])

# FLOAT DIVISION
x = 10
y = 5
print(x/y) # Float Division 2.0
print(x//y) # Floor Division or Integer Division 2

# ABSOLUTE VALUE (Like mathematics)
x = -17
print(abs(x))

# REMAINDER
x = 15 
y = 7
remainder = x % y
print(remainder)


