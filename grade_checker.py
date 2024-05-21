user_input = input("enter a score between 0 - 100: ")
num = int(user_input)
print(type(user_input))

if num > 89:
    print(user_input + ": Grade A")
elif num > 79:
    print(user_input + ": Grade B")
elif num > 69:
    print(user_input + ": Grade C")
elif num > 59:
    print(user_input + ": Grade D")
elif num > 49:
    print(user_input + ": Grade E")
else:
    print(user_input + ": Grade E")