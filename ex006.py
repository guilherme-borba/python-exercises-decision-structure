# Make a Program that reads three numbers and displays the largest of them.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a outher number: "))
num3 = int(input("One more number: "))

largest = 0
if (num1 > num2 and num1 > num3):
    largest = num1
elif (num2 > num1 and num2 > num3):
    largest = num2
else:
    largest = num3

print("Largest number is: ", largest)
