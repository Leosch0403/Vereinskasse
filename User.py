__author__ = 'Leonard Schmid'
import csv
from typing import Union
from Vereinskasse import Club_Accounts

class User:

    def __init__(self, name, password):
        self._name = name
        self._password = password
        self._role = 'user'

    def change_password(self, old_password, new_password):

        if old_password == self._password:
            self._password = new_password
            print('Sie haben das Passwort erfolgreich geändert')
        else:
            print('Sie haben ein falsches Passwort eingegeben')


class Kassenwart(User):

    def __init__(self):
        super().__init__(name, password)
        self.role = 'kassenwart'

class Referent_Finanzen(User):
    pass
