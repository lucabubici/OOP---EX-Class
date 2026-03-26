import subprocess
subprocess.run(['clear'])

print("Hello World")
x = 2
print(x)

age = input('how old are you?')
print(f"You are: {age}")

current_year = int(input("Insert current year."))
year_of_birth = eval(input("What is your year of birth?"))
actual_age = current_year - year_of_birth
print(f"You are {actual_age}")

x = 5
y = 3.4
z = "Hello"
k = "45"
print(float(x))
print(str(x))
print(int(y))
print(int(z))
print(int(k))

#  Simulataineous Assignment
x, y = 1, "Hello"
print(x, y)

x, y = 1,2
x, y = y, x
print(x, y)



