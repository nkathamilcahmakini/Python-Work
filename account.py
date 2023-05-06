class Bank:
    account_type = "Savings"
    
    def __init__(self, account_number, balance, interest_rate):
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful. New balance: {self.balance}"
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawal successful. New balance: {self.balance}"
        else:
            return "Insufficient funds."
        
    def calculate_interest(self, time):
        interest = (self.balance * self.interest_rate * time) / 100
        return f"Interest for {time} years: {interest}"
