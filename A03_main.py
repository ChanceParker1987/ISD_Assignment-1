"""
Description: A client program written to verify implementation 
of the Observer Pattern.
Author: ACE Faculty
Edited by: Chance Parker
Date: October 27, 2024
"""

# 1.  Import all BankAccount types using the bank_account package
from bank_account import *

#     Import date
from datetime import date

#     Import Client
from client.client import Client

# 2. Create a Client object with data of your choice.
client1 = Client(392475, "Chance", "Parker", "cparker2@academic.rrc.ca")

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
chequing_account1 = ChequingAccount(111111, 392475, 870.05, date.today(), 500.00, 0.02)

# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
savings_account1 = SavingsAccount(222222, 392475, 250.00, 200.00, date.today())

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
chequing_account1.attach(client1)

# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
savings_account1.attach(client1)

# 5a. Create a second Client object with data of your choice.
client2 = (123456, "Laurie", "Cutrone", "lcutrone@rrc.ca")

# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
savings_account2 = SavingsAccount(333333, 123456, 100000.00, 50.00, date.today())

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

try:
    chequing_account1.deposit(200.00)  
except ValueError as e:
    print(e)

try:
    chequing_account1.withdraw(820.05)  
except ValueError as e:
    print(e)

try:
    chequing_account1.deposit(10500.00)  
except ValueError as e:
    print(e)

try:
    savings_account1.withdraw(100.00)  
except ValueError as e:
    print(e)

try:
    savings_account1.deposit(15000.00)  
except ValueError as e:
    print(e)

try:
    savings_account1.withdraw(500.00)  
except ValueError as e:
    print(e)

try:
    savings_account2.deposit(5000.00)  
except ValueError as e:
    print(e)

try:
    savings_account2.withdraw(100000.00)  
except ValueError as e:
    print(e)

try:
    savings_account2.withdraw(4950.00)  
except ValueError as e:
    print(e)

