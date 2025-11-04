class Account:
    def __init__(self, acc_no,name,balance=0):
        self._balance = 0
        self.acc_no = acc_no
        self.name = name
    
    def deposit(self,amount):
        if amount>0:
          self._balance += amount
        
        else:
            print('Invalid Amount')
    
    def withdraw(self,amount):
        if self._balance==0:
            print('Insufficient Balance')
        else:
            self._balance=-amount
    
    def get_balance(self):
        return self._balance

if __name__ == '__main__':
    acc1 = Account(123,'Alex',0)
    acc1.deposit(1000)
    print(acc1.get_balance())
    acc1.withdraw(500)
    print(acc1.get_balance())


