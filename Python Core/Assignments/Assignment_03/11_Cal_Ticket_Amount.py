# 11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

# Using While Loop 
'''
Ticket = int(input("Enter the Ticket Price : "))
total_person = 5
total_amount = 0

while (total_person > 0):
        person_age = int(input("Enter the age of person1 : "))
        if(person_age > 0):
                if (person_age < 12 ):
                        total_amount += Ticket*0.7
                elif (person_age > 59):
                        total_amount += Ticket*0.5
                else:
                        total_amount += Ticket
        total_person -= 1
print(f"Total Ticket amount is {total_amount}")
'''
    




