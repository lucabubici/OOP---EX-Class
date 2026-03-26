# print("Paint the wall")
# print("Paint the wall")
# print("Paint the wall")
# print("Paint the wall")

# for painting in range (1, 5):
#     print("Painting day: ", painting)

# for car_speedometer in range(0, 50, 10):
#     print("The car speed is", car_speedometer)

# for car_speedometer in range(100, -1, -10):
#     print("The car speed is: ", car_speedometer)

# timtams = 5

# while timtams > 0:
#     print(f"I have " + str(timtams) + " timtams left")
#     timtams -= 1 #best practise
#     # timtams = timtams - 1 #alternative

# age = 56
# while age >= 18:
#     print("Welcome into the pub")
#     break
# else:
#     print("Bouncer said no. You stayed home.")

# calculate = input("Do you want to calculate your commissions? (y/n) :")

# while calculate == "y":
#     sales = eval(input("Enter yoyur sales amount in AUD: "))
#     commission = eval(input("Enter your commission rate (as a percentage): "))
#     commission = commission / 100 * sales
#     print(f"Your commission is ${commission}")
#     calculate = input("Do you want to calculate your commission again? (y/n)")

# for person in ["Alice", "Bob", "Charlie"]:
#     print(f"Here is a sausage sizzle, ", person)

# for temperature in [25, 30, 35]:
#     print("The current temperature is ", temperature)

# SENTINELS
# items = ['Apple', 'Chocolate', 'Steak', 'Water']

# while True:
#     item = input("Enter item in your cart. Or type Q to quit: ")

#     if item in items:
#         print(f"You have added {item} to your list.")

#     else:
#         print(f"The item {item} is not found in the shopping cart.")
    
#     if item == "Q":
#         quit()

# while True:
#     item = input("Enter item in your cart. Or type Q to quit: ")

#     if item in items:
#         print(f"You have added {item} to your list.")

#     elif item == "Q":
#         print("Program exited.")
#         break
#     else:
#         print(f"The item {item} is not found in the shopping cart.")
    
for workout_set in range(1,4):
    for reps in range(1,11):
        print("Workout Number", workout_set, "Pushups", reps)