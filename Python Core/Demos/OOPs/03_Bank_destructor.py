class BankAccount:
    def __init__(self,ac_no,balance,holder_name):
        self.ac_no = ac_no
        self.bal = balance
        self.holder_nm = holder_name

    def display(self):
        data = f'Accout_no : {self.ac_no}\nBalance : {self.bal}\nHolder_name : {self.holder_nm}'
        return data
    
    def __del__(self):
        print("This is destructor")

b1 = BankAccount(10001,151,"Penduran")
# del b1    
res = b1.display()
print(res)