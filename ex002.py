# Write a Program that asks for a value and shows on the screen whether the value is positive or negative.

number = int(input("Enter a value: "))

if (number > 0):
    print("The number is positive!")
elif (number < 0):
    print("The number is negative!")
else:
    print("The number is neutral")
