# age = 40
# price = 19.99
# first_name = "Chase"
# is_online = True
# print(age)
# name = input("What is your name? ")
# print("Hello " + name)
# birth_year = input("What is your birth year? ")
# age = 2023 - int(birth_year)
# print("You are " + str(age) + " years old.")

# Conversion functions
# int() integer
# bool() boolean
# float() decimal
# str() string

# num1 = input("What is the first number? ")
# num2 = input("What is the second number? ")
# sum = float(num1) + float(num2)
# print("Sum: " + str(sum))

# course = 'Python for Beginners'
# print(course.upper())
# print(course.lower())
# print(course.find('y'))
# print(course.replace('for', '4'))
# print('Python' in course)

# print(20 + 1)
# print(20 -1)
# print(20 * 2)
# print(20 / 3)
# print(20 // 3)
# print(20 % 3)
# print(20 ** 3)

# x = 3 > 2
# x = 3 < 2
# x = 3 <= 2
# x = 3 >= 2
# x = 3 == 2
# x = 3 !=2
# print(x)

# Logical Operators
# price = 25
# print(price > 10 and price < 30)
# print(10 < price < 30)
# print(price < 10 or price > 20)
# print(not price < 10)

# If Statements
# temperature = 35
# if temperature > 80:
#     print("It's a hot day.")
#     print("Drink plenty of water.")
# elif temperature > 60:
#     print("It's a nice day.")
# elif temperature > 45:
#     print("It's a little chilly.")
# else:
#     print("It's cold, man.")
# print("Done.")

# weight = input("Weight: ")
# unit = input("(K)g or (L)bs? ")
# if unit.upper() == "K":
#     converted = float(weight) / .45
#     print("Weight in Lbs: " + str(converted))
# else:
#     converted = float(weight) * 0.45
#     print("Weight in Kgs: " + str(converted))
# print("Done.")

# While Loops
# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1
# while i <= 10:
#     print(i * '*')
#     i = i + 1

# Lists
# names = ["Chase", "John", "Bob", "Mary"]
# print(names)n
# print(names[0])
# print(names[-1])
# names[0] = "Bill"
# print(names)
# print(names[0:3])
# print(len(names))
# print(names[2:])
# names.append('Kyle')
# print(names)
# names.insert(2, 'Jenny')
# print(names)
# names_2 = ['Gary', 'Harry', 'Sally']
# names.insert(0, names_2)
# print(names)
# names.extend(names_2)
# print(names)
# names.remove('Mary')
# print(names)
# names.pop()
# print(names)
# popped = names.pop()
# print(popped)
# names.reverse()
# print(names)
# names.sort()
# print(names)
# names.sort(reverse=True )
# print(names)
# sorted_names = sorted(names)
# print(sorted_names )
# print("Chase" in names)
# for index, name in enumerate(names, start=1):
#     print(index, name)

# Objects
# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# numbers.append(6)
# print(numbers)
# print(1 in numbers)
# numbers.insert(0,"one")
# print(numbers)
# numbers.remove(3)
# print(numbers)
# print(len(numbers))
# numbers.clear()
# print(numbers)
# print(len(numbers))
# print(sum(numbers))


# Iteration
# numbers = [1, 2, 3, 4, 5]
# for item in numbers:
#     print(item)
#
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1

# Range
# # Setting a range of numbers starting at 1 but ending before 5
# numbers = range(5)
# print(numbers)
# for number in numbers:
#     print(number)
#
# # Setting a range of numbers from 5 to 9
# numbers = range(5, 10)
# print(numbers)
# for number in numbers:
#     print(number)
#
# # Setting a range of numbers from 5 to 10, but every 2nd number
# numbers = range(5, 10, 2)
# print(numbers)
# for number in numbers:
#     print(number)
#
# for number in range(6):
#     print(number)

# Tuples
# Tuples are immutable
# numbers = (1, 2, 3, 3)
# print(numbers.count(3))
courses = ['Math', 'English', 'History', 'Art']
courses_string = ', '.join(courses)
print(courses_string)