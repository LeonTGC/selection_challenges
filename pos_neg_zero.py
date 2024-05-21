# Write a program that takes a number as 
# input from the user and prints 
# whether the number is positive, 
# negative, or zero.

user_input = input("enter a number: ")
num = int(user_input)

if num > 0:
    print(user_input + " is positive")
elif num < 0:
    print(user_input + " is negative")
else:
    print(user_input + " is zero")
