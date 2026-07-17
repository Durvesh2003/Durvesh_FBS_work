def addEmp(id,name,sal,dept):
    if (id not in emp_details):
        emp_details[id] = [id,name,sal,dept]
        return 'Employee added Successfully '
    else:
        return (f"{id} already available")
    
def updEmp(id,name,sal,dept):
    if (id in emp_details):
        emp = emp_details[id]
        print("Note : If dont want to change the field leave Blank.")
        name = input(f"enter new name({emp[1]}):") or emp[1]
        sal = float(input(f"enter new sal({emp[2]}):")) or emp[2]
        dept = input(f"enter new name({emp[3]}):") or emp[3]
        emp_details[id] = [id,name,sal,dept]
        return f"Employee updated Successfully"
    else:
        return f'{id} id not exist'

ch = 0
emp_details = {}
while(ch != '6'):
    print(""" Please Select option:
          1. Add Emp
          2. Display Emp
          3. Update Emp
          4. Delete Emp
          5. Search Emp
          6. Exit
          """)
    ch = input("Enter Choice :")
    if(ch == '1'):
        id = input("Enter ID : ")
        name = input("Enter name : ")
        sal = float(input("Enter salary : "))
        dept = input("Enter department :")
        res = addEmp(id,name,sal,dept)
        print(res)
    elif(ch == '2'):
        print(emp_details)
    elif(ch == '3'):
        id = input("Enter the id :")
        res = updEmp(id)
        print(res)
    elif(ch == '4'):
        pass
    elif(ch == '5'):
        pass
    elif(ch == '6'):
        print("Mandal Abhari Aahe !!!!!!")
    else:
        print("Invalid Choice")
