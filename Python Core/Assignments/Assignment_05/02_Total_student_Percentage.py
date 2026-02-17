# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

#          LOGIC----------------
# 1. Input number of students (n)
# 2. sum_percentage = 0
# 3. Repeat n times:
#       Input 5 subject marks
#       total = sum of 5 marks
#       percentage = total / 5
#       print percentage
#       sum_percentage += percentage
# 4. average = sum_percentage / n
# 5. print average

n = int(input("Enter the number 0f students : "))
sum_percentage = 0
for i in range (1,n+1):
    a = int(input("Enter the marks of English : "))
    b = int(input("Enter the marks of Maths : "))
    c = int(input("Enter the marks of Science : "))
    d = int(input("Enter the marks of Hindi : "))
    e = int(input("Enter the marks of CS : "))
    total = a+b+c+d+e
    individual_average = (total)/5
    print("Average of each student", individual_average)

    sum_percentage += individual_average

Total_percentage = sum_percentage/n
print(f"Total Percentage of Student is : {Total_percentage}")



