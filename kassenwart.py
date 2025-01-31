from Vereinskasse import Club_Accounts
from User import User

class Kassenwart(User):
    role: str = 'kassenwart'

    def __init__(self, name, password, account: Club_Accounts):
        super().__init__(name, password)
        self.account = account

    def deposit_money(self, amount: float, description: str):
        self.account.deposit_money(amount)
        print(f"Deposited money: {amount} - {description}")

    def remove_money(self, amount: float, description: str):
        self.account.remove_money(amount)
        print(f"Removed money: {amount} - {description}")
