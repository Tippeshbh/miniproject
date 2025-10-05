class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0 #encapsulation
    
    def check_balance(self):
        print(f"Balance: {self._balance}")
    
    def deposit(self, amount):
        self._balance += amount
        print(f"deposit successful {self._balance}")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"withdraw successful. Updated balance: {self._balance}")
        else:
            print("balance is less than ask")    

   
class savingsAccount(Account): # inheritance
    def calculate_intrest(self):
        INTEREST_RATE = 0.04  # 4%
        intrest =self._balance * INTEREST_RATE
        print(f"Intrest : {intrest}")
    

class CurrentAccount(Account):
    def withdraw(self,amount): # polymorphism
        OVERDRAFT_LIMIT = 1000
        if self._balance  +  OVERDRAFT_LIMIT>= amount:
            self._balance -= amount
            print(f"withdraw successful. Updated Balance: {self._balance}")
        else:
            print("over the limit")

class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__accounts ={}

    def create_account(self, id, holder_name, type):
        if type =="savings":
            new_account = savingsAccount(id, holder_name)  
        else:
            type=="Current"
            new_account =CurrentAccount(id, holder_name)
        self.__accounts[id] = new_account
        print("Account crearion successful")
        return new_account

    def get_account(self, id):
        if id not in self.__accounts:
            print("account not found")
            return None
        else:
            account = self.__accounts[id]
            print(f"\n ID: {account.id} \n Holder Name: { account.holder_name} ")
            return account
        
canara = Bank("Tippesh Bank of Karnataka", " davangere") 

s1 = canara.create_account("1", "karthik", "savings")
c1 = canara.create_account("2", "Virat" , "current")

s1.deposit(1000)
c1.deposit(10)

s1.withdraw(2000)
c1.withdraw(20)

s1.calculate_intrest()


