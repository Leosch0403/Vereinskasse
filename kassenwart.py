
from Vereinskasse import Club_Accounts

lst_of_departments = []
test_account = Club_Accounts('Schwimmen', 45)
print(test_account._department)
snd_account = Club_Accounts('test', 33.2)
lst_of_departments.append(test_account)
lst_of_departments.append(snd_account)
print(lst_of_departments)

print(lst_of_departments[0].get_information())

search = 'test'
for i in range(len(lst_of_departments)):
    if lst_of_departments[i]._department == search:
        print(f"Das Objekt ist an {i} ter Stelle und heißt {lst_of_departments[i]._department}")

class Kassenwart:
    def __init__(self):
        self.transactions = []
        self.balance = 0.0

    def add_transaction(self, amount, description):
        """Add a transaction to the ledger."""
        # ER muss die lst_of_departments durchegehen. Dann muss er das Department suchen was den gleichen Namen wie description hat.
        # Dann muss er deposit money aufrufen
        test.deposit_money()
        self.transactions.append({'amount': amount, 'description': description})
        self.balance += amount
        print(f"Transaction added: {description} of amount {amount}. New balance: {self.balance}")

    def view_balance(self):
        """Return the current balance."""
        return self.balance

    def generate_report(self):
        """Generate a report of all transactions."""
        report = "Transaction Report:\n"
        for transaction in self.transactions:
            report += f"{transaction['description']}: {transaction['amount']}\n"
        report += f"Total Balance: {self.balance}"
        return report

lst_of_departments = []
# Example usage
if __name__ == "__main__":
    test = Club_Accounts('Schwimmen', 35)
    lst_of_departments.append(test)


    kassenwart = Kassenwart()
    kassenwart.add_transaction(100, "Initial Deposit")
    kassenwart.add_transaction(-20, "Purchase Supplies")
    print(kassenwart.view_balance())
    print(kassenwart.generate_report())