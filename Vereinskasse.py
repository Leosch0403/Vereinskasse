'''Defines Classes that are used to simulate accounts of departments of a Club'''

__author__ = "8569130, Schmid, 7996364, Salehi"
import ast

class Clb_dep_acc:
    '''
    This class represents a club department's account, storing information
    such as the department's name, balance, and transaction history.
    It provides methods to deposit, remove money, and manage department accounts.
    '''

    lst_of_dep =[]  # List to store all department account objects

    def __init__(self, department : str, balance : int | float, trans_history=None):
        if trans_history is None:
            new_trans_history = [[round(balance, 2), 'Initiale Einzahlung']]
        else:
            new_trans_history = ast.literal_eval(trans_history)  # Turns input into list
        Clb_dep_acc.lst_of_dep.append(self)
        self._dep_name = department.lower()
        self.balance = round(balance, 2)
        self.transactions = new_trans_history  # Turns input into list


    def get_information(self):
        '''
        Retrieves the current information about the department's attributes
        '''
        return (f"Der Kontostand der Abteilung {self._dep_name} ist {self.balance}€, "
                f"die Transaktionshistorie ist {self.transactions}.")

    def deposit_money(self, amount : int | float, reason):
        '''
        Deposits money into the department's account and records the transaction.

        Args:
            amount (int | float): The amount to be deposited.
            reason (str): The reason for the deposit.
        '''
        # Check whether input data is convertable to float
        try:
            amount = float(amount)
        except ValueError:
            return f"Der Input war keine Zahl"

        amount = round(amount, 2)  # Round the amount to two decimal places
        if amount < 0:
            return f"Der Betrag muss positiv sein."
        # Add the amount and reason to attributes
        self.balance += amount
        self.transactions.append([amount, reason])
        return (f"Aufgrund von {reason} wurde {amount}€ in das Konto der {self._dep_name} "
                f"Abteilung eingezahlt. Neuer Kontostand: {self.balance}€")

    def remove_money(self, amount : int | float, reason):
        '''
        Removes money from the department's account and records the transaction.

        Args:
            amount (int | float): The amount to be removed.
            reason (str): The reason for the withdrawal.
        '''
        # Check whether input data is convertable to float
        try:
            amount = float(amount)
        except ValueError:
            return f"Der Input war keine Zahl"

        amount = round(amount, 2)
        # Check whether input is below 0 or bigger than the balance
        if amount < 0:
            return "Die eingegebene Zahl muss positiv sein."
        if amount > self.balance:
            return f"Der Betrag überschreitet den aktuellen Kontostand von {self.balance}."
        self.transactions.append([-amount, reason])  # Record the withdrawal transaction
        self.balance -= amount
        return (f"{amount}€ wurde von dem Konto der {self._dep_name} Abteilung abgebucht. "
              f"Neuer Kontostand: {self.balance}€")

    @classmethod
    def del_department(self, name):
        """
        Deletes a department's account and removes it from the list of departments.

        Args:
        name (str): The name of the department to be deleted.
        """
        name = name.lower()
        # Loop through all departments
        for dep in Clb_dep_acc.lst_of_dep:
            if name == dep._dep_name:
                Clb_dep_acc.lst_of_dep.remove(dep)  # Remove the department from the list
                return f"Konto der Abteilung {name} wurde gelöscht."
        return f"Konto der Abteilung {name} konnte nicht gefunden werden und wurde nicht gelöscht."

if __name__ == '__main__':
    account1 = Clb_dep_acc("Abteilung 1", 1000, [500, -30])
    account2 = Clb_dep_acc("Abteilung 2", 1500)
    account3 = Clb_dep_acc("Abteilung 2", 500)