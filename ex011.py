'''Tabajara Organizations decided to give its employees a salary increase and hired him to develop 
the program that will calculate the adjustments.
Create a program that receives an employee's salary and readjusts it according to the following criteria, 
based on the current salary:
1) salaries up to R$280.00 (inclusive): 20% increase
2) salaries between R$280.00 and R$700.00: 15% increase
3) salaries between R$700.00 and R$1500.00: 10% increase
4) salaries from R$1500.00 onwards: 5% increase After the increase is made, inform on the screen:
5) the salary before the adjustment;
6) the percentage of increase applied;
7) the amount of the increase;
8) the new salary, after the increase.'''

salary = float(input("Value of salary: "))

if (salary < 280):
    increase = 20
    newSalary = salary + (salary * increase / 100)
elif (salary >= 280 and salary < 700):
    increase = 15
    newSalary = salary + (salary * increase / 100)
elif (salary >= 700 and salary < 1500):
    increase = 10
    newSalary = salary + (salary * increase / 100)
elif (salary >= 1500):
    increase = 10
    newSalary = salary + (salary * increase / 100)

print("Salary before the adjustment: $", salary)
print(f"Percentage of increase applied: {increase}%")
print(f"Amount of the increase: $ {(newSalary - salary):.2f}")
print(f"New salary, after the increase: $ {newSalary:.2f}")
