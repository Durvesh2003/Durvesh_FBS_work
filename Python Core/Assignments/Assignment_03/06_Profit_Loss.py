# 6. Write a program to calculate profit or loss.
CP = int(input("Enter the cost price : "))
SP = int(input("Enter thhe Selling price : "))

if (SP > CP):
    profit = SP - CP
    print(f"Profit of Rs.{profit}")
else:
    Loss = CP-SP
    print(f"Loss of Rs.{Loss}")