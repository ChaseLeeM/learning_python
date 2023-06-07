# age = 40
# price = 19.99
# first_name = "Chase"
# is_online = True
# print(age)
name = input("What is your name? ")
print("Hello " + name)
birth_year = input("What is your birth year? ")
age = 2023 - int(birth_year)
print("You are " + str(age) + " years old.")

# Conversion functions
# int() integer
# bool() boolean
# float() decimal
# str() string

num1 = input("What is the first number? ")
num2 = input("What is the second number? ")
sum = float(num1) + float(num2)
print("Sum: " + str(sum))