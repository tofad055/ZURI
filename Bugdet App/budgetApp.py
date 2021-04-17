
class Budget:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    


    def deposit(self, amount):
        old_balance = self.balance
        self.balance = self.balance + amount

        return f'Old: {old_balance}, New: {self.balance}'

    def withdraw(self, amount):

        if self.balance < amount:
            return 'you dont have enough cash'
        else:
            old_balance = self.balance
            self.balance = self.balance - amount

            return f'Old: {old_balance}, New: {self.balance}'

    def get_balance(self):
        feedack = "your balance is %d, % self.balance"
        
        return feedback
    def transfer(self, amount, transfer_to):
        if self.balance < amount:
            return "you dont have enough funds"
        else:
            self.balance = self.balance - amount
            transfer_to.balance = transfer_to.balance + amount

            feedback = f"you transferrred ${amount} to {transfer_to.name} budget \n"
            feedback += f"The balance for {self.name} is now {self.balance} while \n"
            feedback += f"The balance for {transfer_to.name} is now {transfer_to.balance}"  
            return feedback
food_Budget = Budget("food", 2000)
clothing_Budget = Budget("clothing", 3000)
entertainment_Budget = Budget("entertainment", 5000)
