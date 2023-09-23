# Write a program that asks for two numbers and prints the largest of them.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter other number: "))

if (num1 > num2):
    largestNumber = num1
    print("Largest number: ", largestNumber)
elif (num2 > num1):
    largestNumber = num2
    print("Largest number: ", largestNumber)
else:
    print("Equal numbers")
