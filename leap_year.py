# Write a program that takes a year as 
# input from the user and determines if it is 
# a leap year. A leap year is divisible by 4, 
# but if it is divisible by 100, 
# it should also be divisible by 400.

user_input = input("enter a year: ")
year = int(user_input)

if year % 4 == 0:
    print(user_input + " is a leap year")
else:
    if year % 100 == 0 and year % 400 == 0:
        print(user_input + " is a leap year")
    else:
        print(user_input + " is not a leap year")

    