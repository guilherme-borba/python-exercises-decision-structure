# Make a Program that reads three numbers and displays them in descending order.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a outher number: "))
num3 = int(input("One more number: "))

largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)
avg = (num1 + num2 + num3) - (largest + smallest)

print(f"Descending order: {largest}, {avg} e {smallest}")
