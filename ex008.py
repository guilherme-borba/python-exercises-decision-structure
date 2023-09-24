# Create a program that asks the price of three products and tells you which product you should buy,
# knowing that the decision is always for the cheapest.

price1 = float(input("1° price product: "))
price2 = float(input("2° price product: "))
price3 = float(input("3° price product: "))

cheapest = min(price1, price2, price3)

print("Buy the of: ", cheapest)
