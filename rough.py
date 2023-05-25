def withdraw(self, amount):
        if amount > self.balance:
            return f"Insufficient funds. Your current balance is ${self.balance}"
        else:
            self.balance -= amount
            return f"Your withdrawal of ${amount} was successful. Your new balance is ${self.balance}"
        
def deposit(self, amount):
        self.balance += amount
        return f"Your deposit of ${amount} was successful. Your new balance is ${self.balance}"

def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Your account earned ${interest} in interest. Your new balance is ${self.balance}"        