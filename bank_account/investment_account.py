"""
Description: Module 2 Assignment 2: InvestmentAccount Class
Author: Chance Parker
"""
from datetime import date, timedelta
from client.client import Client
from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """
    InvestmentAccount class: Represents a specific bank account with a 
    management fee.
    Constants:
        TEN_YEARS_AGO (date): Today's date minus 10 years.
        BASE_SERVICE_CHARGE (float): The base service charge for all 
        bank accounts.
    Attributes:
        management_fee (float): The management fee for the account.
    Methods:
        get_service_charges: calculates and returns the service charges 
        based on the age of the account.
    """

    def __init__(self, account_number, client_number, balance, management_fee, 
                 date_created = None):
        super().__init__(account_number, client_number, balance, 
                         date_created)
        """
        Initializes the InvestmentAccount object on recieved arguments
        (if valid). Inherits from the BankAccount class.
        args:
            account_number (int): The account's unique id.
            client_number (int): The client's unique id.
            balance (float): The balance of the bank account.
            date_created (date): The date the account was created, defaults to today. 
            management_fee (float): The fee to manage the investment account.
        raises:
            ValueError if any of the arguments are invalid.
        """
        TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
        BASE_SERVICE_CHARGE = 0.50

        if isinstance(management_fee, (int, float)):
            self.__management_fee = float(management_fee)
        else:
            self.__management_fee = 2.55

        self.TEN_YEARS_AGO = TEN_YEARS_AGO
        self.BASE_SERVICE_CHARGE = BASE_SERVICE_CHARGE

    @property
    def management_fee(self)-> float:
        """
        Accessor for the management_fee sttribute.
        Returns: float - The management fee for the account.
        """
        return self.__management_fee 

    def __str__(self)-> str:
        """
        Returns a string representation of the InvestmentAccount instance.
        Returns: str - The investment account instance as a formatted string.
        """ 
        account_info = super().__str__()

        if self.date_created < self.TEN_YEARS_AGO:
            management_fee_str = "Waived"
        else:
            management_fee_str = f"${self.__management_fee:.2f}"

        return (f"{account_info}\nDate Created: {self.date_created}"
                f"Management Fee: {management_fee_str} Account Type: Investment")
    
    def get_service_charges(self)-> float:
        """
        Calculates the service charges based on the age of the account.
        Returns: float - The calculated service charge.
        """
        if self.date_created < self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + self.__management_fee
        
               

