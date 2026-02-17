# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

############ LOGIC ######
# 1. Input number of passengers (n)
# 2. Input ticket cost
# 3. total_amount = 0
# 4. Repeat n times:
#       Input age
#       If age < 12:
#             apply 30% discount
#       elif age > 59:
#             apply 50% discount
#       else:
#             full ticket
#       Add passenger amount to total_amount
# 5. Print total_amount

Passengers = int(input("Enter the number of Passeners : "))
Ticket = int(input("Enter the Ticket Amount : "))

Total_Ticket_Amount = 0
for i in range (1,Passengers+1):

    age = int(input("Enter the age "))

    if (age < 12):
            Total_Ticket_Amount += Ticket * 0.7

    elif (age > 59):
            Total_Ticket_Amount += Ticket * 0.5

    else :
            Total_Ticket_Amount += Ticket
        

print(f"Total Ticket is : {Total_Ticket_Amount}")