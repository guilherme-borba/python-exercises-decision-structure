# Make a Program that reads three numbers and shows the largest and smallest of them.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a outher number: "))
num3 = int(input("One more number: "))

largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

print("Largest number is: ", largest)
print("Smallest number is: ", smallest)
