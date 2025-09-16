#####################Python Primitive Data Types#############################################

# # subscripting
# print("Hello"[0])
# print("Hello"[1])
# print("Hello"[-1])
# print("Hello"[-2])

# # string
# print("123"+"345")    # concatenation

# # Integer = whole number
# print(123)
# print(123 + 345)

# # large Integer
# print(123456789)
# print(123_456_789)

# # Float = floating point number
# print(3.14159)

# # Boolean
# print(True)
# print(False)

#####################Type Error, Type Checking and Type Conversion#############################################

# # # Type Error

# len("hello")
# # len(123)        # Type Error

# # Type Checking

# print(type(123))
# print(type(123.456))
# print(type("hello"))
# print(type(True))

# # Type Conversion

# print(123 + 456)
# print("123" + "456")
# print(int("123") + int("456"))
# # print(int("abc") + int("456"))      # Value Error

#####################Mathematical Operations in Python#############################################

# # # Operations in Python

# print("My age: " + str(12))         # concatenation
# print(123 + 456)                    # Subtraction
# print(7 -3 )                        # Addition
# print(3 * 2)                        # Multiplication
# print(6 /3 )                        # Division (implicit type casting)
# print(6 // 3)                       # Division
# print(5 / 3)                        # Division (implicit type casting)
# print(5 // 3)                       # Division
# print(2 ** 3)                       # Exponentiation

# # # Priority of operation : PEMDAS (Parentheses , Exponentiation , Multiplication / Division , Addition / Subtraction )
# # # order of operation in python: left to right

# print(3 * 3 + 3 / 3 - 3)
# print(3 * (3 + 3 )/ 3 - 3) 

#####################Number Manipulation and F Strings in Python#############################################

# # # Round function

# bmi = 84 / 1.65 ** 2
# print(bmi)

# print(int(bmi))

# print(round(bmi))

# print(round(bmi,2))

# # # Assigment operator (+=,-=,*=,/=,%=)

# score = 1 

# # user score 2 point
# score += 2

# print(score)

# # # fstring

# score = 0
# height = 1.8
# is_winning = True

# print(f"your score = {score} ,height = {height} , winning = {is_winning}")


#####################Project#############################################

# # Day 2 Project: Tip Calculator

# print("Welcome to the tip calculator!")

# bill = float(input("What is the total bill amount?\n$:"))
# tip = int(input("How much tip would you like to give?\nPercent:"))
# split = int(input("How many people to split the bill?\nPeople:"))

# total = ("{:.2f}".format((((bill * (tip / 100)) + bill) / split)))

# print(f"Each person should pay: ${total}")

# # or # #

# Day 2 Project: Tip Calculator

print("Welcome to the tip calculator!")

bill = float(input("What is the total bill amount?\n$:"))
tip = int(input("How much tip would you like to give?\nPercent:"))
split = int(input("How many people to split the bill?\nPeople:"))

total = round((((bill * (tip / 100)) + bill) / split),2)

print(f"Each person should pay: ${total}")