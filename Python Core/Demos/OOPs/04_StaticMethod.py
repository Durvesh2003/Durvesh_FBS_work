class BankAccount:
    Branch = "SBI Acc"
    def __init__(self,ac_no,balance,holder_name):
        self.ac_no = ac_no
        self.bal = balance
        self.holder_nm = holder_name

    def display(self):
        data = f'Accout_no : {self.ac_no}\nBalance : {self.bal}\nHolder_name : {self.holder_nm}'
        return data
    
    @staticmethod
    def displayBranch():
        return BankAccount.Branch

b1=BankAccount(10001,151,"Penduran")  
res = b1.display()
print(res)

# print(BankAccount.Branch)
print(BankAccount.displayBranch())