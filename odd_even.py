#  Write a program that takes an integer
# input from the user and prints whether 
# the number is odd or even.

user_input = input("enter a number: ")

if int(user_input) % 2 == 0:
    print("the number " + user_input + " is even")
else:
    print("the number " + user_input + " is odd")

