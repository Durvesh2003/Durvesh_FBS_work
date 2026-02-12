# 11. Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount.
    
amount = int(input("Enter the amount : "))

notes = [2000,1000,500,200,100,50,20,10,5,2,1]

for note in notes:
    if amount >= note:
        count = amount // note
        amount = amount % note
        print(f"{note} : {count}")
