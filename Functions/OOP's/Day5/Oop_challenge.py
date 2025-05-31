class Account:
    def __init__(self,owner,balance=0):
      self.owner=owner
      self.balance=balance
    def deposit(self,dept_amt):
        self.balance=self.balance+dept_amt
        print(dept_amt)
    def withdraw(self,wd_amt):
      if self.balance>=wd_amt:
          self.balance-=wd_amt
          print("Withdrawan success")
      else:
          print("No Money")
acc=Account("Jose",100)
acc1=Account("Rose",100)
print(acc.deposit(56))
print(acc.owner)
print(acc.balance)
print(acc.withdraw(250))
    