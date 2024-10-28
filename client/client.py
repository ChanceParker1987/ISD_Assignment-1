"""
Description: Module 1 Assignment 1: Client Class
Author: Chance Parker
"""
import email_validator
from email_validator import validate_email
from email_validator import EmailNotValidError

class Client:
    """
    Client class. Represents a client in a bank.
    Attributes:
        __client_number(int): The client's unique id.
        __first_name(str): The first name of the client.
        __last_name(str): The last name of the client.
        __email_address(str): The email address of the client.
    Methods:
        __init__(): Initializes class attributes.
        client_number(): Client number accessor.
        first_name(): First name accessor.
        last_name(): Last name accessor.
        email_address(): Email address accessor.
        __str__: Returns a string representaion of the class. 
    """
    def __init__(self, client_number: int, first_name: str, 
                 last_name: str, email_address: str):
        """
        Initializes a client object on received arguments (if valid).
        args:
            client_number (int): The client's unique id.
            first_name (str): The first name of the client.
            last_name (str): The last name of the client.
        raises:
            ValueError if any of the arguments are invalid.
        """
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be a whole number.")
        
        if len(first_name.strip()) > 0:
            self.__first_name = first_name
        else:
            raise ValueError("First name cannot be blank.")
        
        if len(last_name.strip()) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last name cannot be blank.")
        
        if validate_email(email_address, check_deliverability = False):
            self.__email_address = email_address
        else:
            raise EmailNotValidError("Email is not a valid format.")
        
    @property
    def client_number(self) -> int:
        """
        Accessor for the client_number attribute.
        Returns: int - The unique id associated with the Client instance.
        """
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """
        Accessor for the first_name attribute.
        Returns: str - The first name associates with the Client instance.
        """
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """
        Accessor for the last_name attribute.
        Returns: str - The last name associated with the Client instance
        """
        return self.__last_name

    @property
    def email_address(self) -> str:
        """
        Accessor for the email_address attribute.
        Returns: str - The email address associated with the Client instance
        """
        return self.__email_address
    
    def __str__(self) -> str:
        """
        Returns a string representation of the Client instance.
        Returns: str - The Client instance as a formatted string.
        """
        return (f"{self.__last_name}, {self.__first_name}"
                + f"[{self.__client_number}] - {self.__email_address} ")