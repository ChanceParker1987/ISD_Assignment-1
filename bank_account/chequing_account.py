"""
Description: Module 2 Assignment 2: ChequingAccount Class
Author: Chance Parker
"""
from datetime import date
from client.client import Client
from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    """
    ChequingAccount class: Represents a specific type of bank account with 
    an overdraft.
    Attributes:
        overdraft_limit (float): The overdraft limit of the account.
        overdraft_rate (float): The interest rate for the overfraft amount.
    Methods:
        get_service_charges (float): calculates and returns the service charges 
        for the account based on the balance, overdraft_limit and overdraft_rate.
    """

    def __init__(self, account_number: int, client_number: int, 
                 balance: float, date_created: date = None, 
                 overdraft_limit: float = 0.0, overdraft_rate: float = 0.0):
        super().__init__(account_number, client_number, balance, date_created)

        if isinstance(overdraft_limit, (int, float)):
            self.__overdraft_limit = float(overdraft_limit)
        else:
            self.__overdraft_limit = -100.0

        if isinstance(overdraft_rate, (int, float)):
            self.__overdraft_rate = float(overdraft_rate)
        else:
            self.__overdraft_rate = 0.05


    @property
    def overdraft_limit(self)-> float:
        """
        Accessor for the overdraft_limit attribute.
        """
        return self.__overdraft_limit
    
    @property
    def overdraft_rate(self)-> float:
        """
        Accessor for the overdraft_rate attribute.
        """
        return self.__overdraft_rate
    
    def get_service_charges(self) -> float:
        """
        Returns the calculated service charges for the ChequingAccount.
        Uses the superclass method for the base charge and adds the specific charges.
        """
        if self.balance >= self.overdraft_limit:
            return super().get_service_charges()
        else:
            overdraft_service_charge = (self.overdraft_limit - self.balance) * self.overdraft_rate
            return super().get_service_charges() + overdraft_service_charge
    
    def __str__(self)-> str:
        """
        Returns a string representation of the ChequingAccount instance.
        Returns: str - The ChequingAccount instance as a formatted string.
        """
        account_info = super().__str__()

        return (f"{account_info}\n"
                f"Overdraft Limit: {self.__overdraft_limit:.2f} Overdraft Rate: " 
                f"{self.__overdraft_rate * 100:.2f}% Account Type: Chequing")

