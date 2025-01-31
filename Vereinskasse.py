__author__ = 'Leonard Schmid'


class Clb_dep_acc:

    lst_of_dep =[]

    def __init__(self, department : str, balance : int | float, trans_history=None):
        if trans_history is None:
            trans_history = []
        Clb_dep_acc.lst_of_dep.append(self)
        self._department = department.lower()
        self.balance = round(balance, 2)
        self.transactions = trans_history

    def get_information(self):
        return (f"Der Kontostand der Abteilung {self._department} ist {self.balance}€, "
                f"die Transaktionshistorie ist {self.transactions}")

    def deposit_money(self, amount : int | float):
        amount = round(amount, 2)
        if amount <= 0:
            raise ValueError("Der Betrag muss positiv sein.")
        self.balance += amount
        print(f"{amount}€ wurde in das Konto der {self._department} Abteilung eingezahlt. "
              f"Neuer Kontostand: {self.balance}€")

        # Es fehlt dass der Betrag self.transactions hinzugefügt wird


    def remove_money(self, amount : int | float):
        amount = round(amount, 2)
        if amount <= 0:
            raise ValueError("Der Betrag muss positiv sein.")
        if amount > self.balance:
            raise ValueError(f"Der Betrag überschreitet den aktuellen Kontostand von {self.balance}.")
        self.balance -= amount
        print(f"{amount}€ wurde von dem Konto der {self.department} Abteilung abgebucht. "
              f"Neuer Kontostand: {self.balance}€")

    @classmethod
    def del_department(self, name):
        """
        Deletes a created object and reduces the total number of objects
        """
        name = name.lower()
        for dep in Clb_dep_acc.lst_of_dep:
            if name == dep._department:
                Clb_dep_acc.lst_of_dep.remove(dep)
                return f"Konto der Abteilung {name} wurde gelöscht."
        return f"Konto der Abteilung {name} konnte nicht gefunden werden und wurde nicht gelöscht."

if __name__ == '__main__':
    account1 = Clb_dep_acc("Abteilung 1", 1000, [500, -30])
    account2 = Clb_dep_acc("Abteilung 2", 1500)
    print(account2.transactions)
    print(account1.transactions)
    print(Clb_dep_acc.lst_of_dep)
    print(Clb_dep_acc.del_department('Abteilung 1'))
    print(Clb_dep_acc.del_department('Abteilung f'))
    print(Clb_dep_acc.lst_of_dep)
    print(account2.get_information())