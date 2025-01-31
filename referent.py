class Referent_in_Finanzen(User):
    role: str = 'referent'

    def __init__(self, name, password, account: Club_Accounts):
        super().__init__(name, password)
        self.account = account

    def view_all_transactions(self):
        for transaction in self.account.transactions:
            print(f"{transaction['type'].capitalize()}: {transaction['amount']} - {transaction['description']}")

    def view_transaction_history(self):
        history = f"Transaction History:\n"
        for transaction in self.account.transactions:
            history += f"{transaction['type'].capitalize()}: {transaction['amount']} - {transaction['description']}\n"
        return history

