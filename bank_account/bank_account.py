"""
Description: Module 1 Assignment 1: BankAccount Class
Author: Chance Parker
"""
from client.client import Client
from abc import ABC, abstractmethod
from datetime import date

class BankAccount(ABC):
    """
    BankAccount class: Represents a Client Bank Account.
    Constants:
        BASE_SERVICE_CHARGE (float): The base service charge for all bank accounts.
    Attributes:
        __account_number (int): The unique id of the bank account.
        __client_number (int): The unique id of the client.
        __balance (float): The balance of the bank account.
    Methods:
        __init__(): Initializes the BankAccount object.
        account_number(): Accessor for the account_number attribute.
        client_number(): Accessor for the client_number attribute.
        balance(): Accessor for the balance attribute.
        update_balance(amount: float): Updates the balance of the bank account.
        deposit(amount: float): Deposits funds into the bank account.
        withdraw(amount: float): Withdraws funds from the bank account.
        __str__(): Returns a string representation of the class.
        get_service_charges(float): Returns the BASE_SERVICE_CHARGE.
    """
    BASE_SERVICE_CHARGE: float = 0.50 # Class level constant

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date = None):
        """
        Initializes a BankAccount object on received arguments (if valid).
        args:
            account_number (int): The account's unique id.
            client_number (int): The client's unique id.
            balance (float): The balance of the bank account.
            date_created (date): The date the account was created, defaults to today 
            if not specified.
        raises:
            ValueError if any of the arguments are invalid.
        """

        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be numeric.")
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be numeric.")
        
        try:
            self.__balance = float(balance)
        except (ValueError, TypeError):
            self.__balance = 0.0

        if date_created is None:
            self._date_created = date.today()
        elif not isinstance(date_created, date):
            raise ValueError("date_created is not a valid date instance.")
        else:
            self._date_created = date_created
    
    @property
    def account_number(self) -> int:
        """
        Accessor for the __account_number attribute.
        Returns: int - The unique id associated with the bank_account instance.
        """
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """
        Accessor for the __client_number attribute.
        Returns: int - The unique id associated with the client instance.
        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """
        Accessor for the __balance attribute.
        Returns: float - The balance of the bank acount as a float.
        """
        return self.__balance
    
    @property
    def date_created(self)-> date:
        """
        Accessor for the __date_created attribute
        Returns: date - The date the bank account was created.
        """
        return self._date_created
    
    def update_balance(self, amount: float):
        """
        Updates the balance of the bank account by adding the given amount.
        args:
            amount (float): The amount to add to the balance, can be positive or negative.
        """
        try:
            amount = float(amount)
            self.__balance += amount
        except (ValueError, TypeError):
            print("Invalid amount. Balance remains unchanged.")

    def deposit(self, amount: float):
        """
        Deposits funds as a float into a bank account.
        args:
            amount (float): The amount to be deposited into the bank account"
        """
        if not isinstance(amount, (int,float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Deposit amount: {amount:.2f} must be positive.")
        
        self.update_balance(amount)

    def withdraw(self, amount: float):
        """
        Withdraws funds as a float from a bank account.
        args:
            amount (float): The amount to be withdrawn from the bank account"
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Withdraw amount: {amount:.2f} must be positive.")
        
        if amount > self.__balance:
            raise ValueError(f"Withdraw amount: {amount:.2f} must not exceed the" 
                             + f"account balance: {self.__balance:.2f}.")
        
        self.update_balance(-amount)

    def __str__(self) -> str:
        """
        Returns a string representation of the BankAccount instance.
        Returns: str - The BankAccount instance as a formatted string.
        """
        return (f"Account Number: {self.__account_number} Balance: {self.__balance:.2f}.")
    
    @abstractmethod
    def get_service_charges(self)-> float:
        """
        Returns the service charge for the bank account.
        """
        return self.BASE_SERVICE_CHARGE 
    




        

