__author__ = 'Leonard Schmid'

class Clb_dep_acc:

    lst_of_dep =[]

    def __init__(self, department : str, balance : int | float, trans_history=None):
        if trans_history is None:
            trans_history = [round(balance, 2)]
        Clb_dep_acc.lst_of_dep.append(self)
        self._dep_name = department.lower()
        self.balance = round(balance, 2)
        self.transactions = trans_history

    def get_information(self):
        return (f"Der Kontostand der Abteilung {self._dep_name} ist {self.balance}€, "
                f"die Transaktionshistorie ist {self.transactions}.")

    def deposit_money(self, amount : int | float):
        amount = round(amount, 2)
        if amount < 0:
            return f"Der Betrag muss positiv sein."
        self.balance += amount
        self.transactions.append(amount)
        return (f"{amount}€ wurde in das Konto der {self._department} Abteilung eingezahlt. "
                f"Neuer Kontostand: {self.balance}€")

    def remove_money(self, amount : int | float):
        amount = round(amount, 2) * -1
        if amount < 0:
            return "Die eingegebene Zahl muss positiv sein."
        if amount > self.balance:
            return f"Der Betrag überschreitet den aktuellen Kontostand von {self.balance}."
        self.balance += amount
        return (f"{amount}€ wurde von dem Konto der {self.department} Abteilung abgebucht. "
              f"Neuer Kontostand: {self.balance}€")

    @classmethod
    def del_department(self, name):
        """
        Deletes a created object and reduces the total number of objects
        """
        name = name.lower()
        for dep in Clb_dep_acc.lst_of_dep:
            if name == dep._dep_name:
                Clb_dep_acc.lst_of_dep.remove(dep)
                return f"Konto der Abteilung {name} wurde gelöscht."
        return f"Konto der Abteilung {name} konnte nicht gefunden werden und wurde nicht gelöscht."

if __name__ == '__main__':
    account1 = Clb_dep_acc("Abteilung 1", 1000, [500, -30])
    account2 = Clb_dep_acc("Abteilung 2", 1500)
    account3 = Clb_dep_acc("Abteilung 2", 500)
    print(Clb_dep_acc.lst_of_dep)
    print(Clb_dep_acc.lst_of_dep[0]._ksnwart.get_info())
    print(Clb_dep_acc.lst_of_dep[1]._ksnwart.get_info())
    print(Clb_dep_acc.lst_of_dep[2]._ksnwart.get_info())
    print(Clb_dep_acc.lst_of_dep[1]._ksnwart._department._dep_name)
'''    print(account2.transactions)
    print(account1.transactions)
    print(Clb_dep_acc.lst_of_dep)
    print(Clb_dep_acc.del_department('Abteilung 1'))
    print(Clb_dep_acc.del_department('Abteilung f'))
    print(Clb_dep_acc.lst_of_dep)
    print(account2.get_information())'''