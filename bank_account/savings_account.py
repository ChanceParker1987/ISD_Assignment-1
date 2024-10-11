"""
Description: Module 2 Assignment 2: SavingsAccount Class
Author: Chance Parker
"""
from datetime import date, timedelta
from client.client import Client
from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    """
    SavingsAccount class: Represents a specific bank account with a minimum balance.
    Constants:
        BASE_SERVICE_CHARGE (float): The base service charge for all bank accounts.
        SERVICE_CHARGE_PREMIUM (float): The service charge when minimum balance is not met.
    Attributes:
        minimum_balance (float): The minimum balance for the accoint
    Methods:
        get_service_charges: Calculates and returns the service charges based on whether
        the minimum balance is met or not. 
    """

    def __init__(self, account_number, client_number, balance, minimum_balance, date_created = None):
        super().__init__(account_number, client_number, balance, date_created)
        """
        Initializes the SavingsAccount object on received arguments
        (if valid). Inherits from the BankAccount class.
        args:
            account_number (int): The account's unique id.
            client_number (int): The client's unique id.
            balance (float): The balance of the bank account.
            minimum_balance (float): The minimum balance required for the account.
            date_created (date): The date the account was created, defaults to today. 
        raises:
            ValueError if any of the arguments are invalid.
        """
        BASE_SERVICE_CHARGE = 0.50
        SERVICE_CHARGE_PREMIUM = 2.0

        if isinstance(minimum_balance, (int, float)):
            self.__minimum_balance = float(minimum_balance)
        else:
            self.__minimum_balance = 50.00

        self.BASE_SERVICE_CHARGE = BASE_SERVICE_CHARGE
        self.SERVICE_CHARGE_PREMIUM = SERVICE_CHARGE_PREMIUM

    @property
    def minimum_balance(self) -> float:
        """
        Accessor for the minimum_balance attribute.
        Returns: float - The minimum balance for the account.
        """
        return self.__minimum_balance

    def __str__(self) -> str:
        """
        Returns a string representation of the SavingsAccount instance.
        Returns: str - The savings account instance as a formatted string.
        """ 
        account_info = super().__str__()  

        return (f"{account_info}\n"
                f"Minimum Balance: f{self.__minimum_balance:.2f}\n"
                f"Account Type: Savings")

    def get_service_charges(self) -> float:
        """
        Calculates the service charges based on the account balance.
        Returns: float - The calculated service charge.
        """
        if self.balance > self.__minimum_balance:

            return self.BASE_SERVICE_CHARGE
        else:

            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM