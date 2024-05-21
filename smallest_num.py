# Write a program that takes three numbers 
# as input from the user and prints the 
# smallest of the three.

user_input = input("enter three numbers seperated by spaces: ")
num1 = user_input[0]
num2 = user_input[2]
num3 = user_input[4]
print(num1, num2, num3)

if num1 > num2 and num1 > num3:
    print(num1 + " is the biggest")
elif num2 > num1 and num2 > num3:
    print(num2 + " is the biggest")
else:
    print(num3 + " is the biggest")
