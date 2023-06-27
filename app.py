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

# Conversion functions----------------
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
# Object Identity: is
# print(x)

# Logical Operators---------------
# price = 25
# print(price > 10 and price < 30)
# print(10 < price < 30)
# print(price < 10 or price > 20)
# print(not price < 10)

# If Statements---------------
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

# Lists---------------------
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
# courses = ['Math', 'English', 'History', 'Art']
# courses_string = ' - '.join(courses)
# print(courses_string)
# new_list = courses_string.split(' - ')
# print(new_list)

# Objects-------------------
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


# Iteration----------------
# numbers = [1, 2, 3, 4, 5]
# for item in numbers:
#     print(item)
#
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1

# Range----------------------
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

# Tuples-------------
# my_list = [1, 2, 3]  # List
# my_tuple = (1, 2, 3)  # Tuple

# Modifying elements------------
# my_list[0] = 0  # Lists are mutable
# my_tuple[0] = 0  # This will raise an error since tuples are immutable

# Adding elements------------
# my_list.append(4)  # You can add elements to lists
# my_tuple.append(4)  # Tuples do not have an append method

# Iterating over elements----------
# for item in my_list:
#     print(item)
# for item in my_tuple:
#     print(item)

# Tuple unpacking------------
# x, y, z = my_tuple  # Tuple unpacking is a convenient way to assign values

# List comprehension------------
# squared_list = [x**2 for x in my_list]  # List comprehension is a powerful feature for lists

# Sets----------------
# my_set = {1, 2, 3}  # Set literal
# print(my_set)
# my_set.add(4)  # Adding an element to the set
# print(my_set)
# my_set.remove(2)  # Removing an element from the set
# print(my_set)
# cs_courses = {'history', 'math', 'physics', 'compsci'}
# art_courses = {'history', 'math', 'art', 'design'}
# print(cs_courses.intersection(art_courses))
# print(cs_courses.difference(art_courses))
# print(cs_courses.union(art_courses))

# Empty Lists, Sets and Tuples----------------
# empty_list = []  # Using square brackets
# empty_list = list()  # Using the list() function
#
# empty_set = set()  # Using the set() function
# empty_set = {} # Does not create a set! This creates an empty Dictionary

# empty_tuple = ()  # Using parentheses
# empty_tuple = tuple()  # Using the tuple() function

# Dictionaries ------------------
# student = {'name': 'Chase', 'age': 40, 'courses': ['Python', 'React']}
# print(student)
# print(student['name'])
# print(student['courses'])
# print(student.get('age'))
# print(student.get('phone'))  # Prints none instead of an error
# print(student.get('phone', 'Not Found'))  # Gives back custom message
# student['phone'] = '555-5555'
# print(student.get('phone', 'Not Found'))
# student.update({'name': 'Charles', 'age': 5, 'phone': '123-4567'})
# print(student)
# del student['courses']
# print(student)
# age = student.pop('age')
# print(age)
# print(len(student))
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())
# for key in student:
#     print(key)
# for key, value in student.items():
#     print(key, value)

# Conditionals
# language = 'Java '
# if language == 'Python':
#     print('Language is Python')
# elif language == 'Java':
#     print('Language is Java')
# else:
#     print('No match')

# user = 'Admin'
# logged_in = True
# if user == 'Admin' and logged_in:  # Both variables must be true.
#     print('Admin logged in.')
# else:
#     print("Admin not logged in.")
#
# if user == 'Admin' or logged_in:  # Or will be true if either is true
#     print('Admin logged in.')
# else:
#     print("Admin not logged in.")
#
# if not logged_in:  # If not
#     print('log in.')
# else:
#     print("Welcome " + user + '.')

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))
# b = a
# print(a is b)
# print(id(a))
# print(id(b))
# print(a == b)

# False Values
# False
# None
# Zero of any numeric type
# Any empty sequence. Example : '', (), [].
# Any empty mapping : {}.
# condition = []
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')

# While Loops---------------
# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1
# while i <= 10:
#     print(i * '*')
#     i = i + 1

# For Loops-------------
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     if num == 3:
#         print('Found.')
#         break
#     print(num)
#
# for num in nums:
#     if num == 3:
#         print('Found.')
#         continue
#     print(num)
# for num in nums:
#     for letter in 'abc':
#         print(num, letter)
# for i in range(1, 11):
#     print(i)

# Functions-------------
# def hello_func():
#     pass  # Allows the function to be empty without throwing an error.
#
#
# hello_func()
#
#
# def hello_func2():
#     print('Hello!')
#
#
# hello_func2()

def hello_func3():
    return "Hello"


hello_func3()
print(hello_func3())
print(hello_func3().upper())


def hello_func4(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


print(hello_func4('Hi', name='Chase'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)
