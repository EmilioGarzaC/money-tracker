import os

from database.DDL.fact_movement import factMovement
from database.DDL.dim_date import dimDate
from database.DDL.dim_transactionType import dimTransactionType
from database.DDL.dim_moneyGroup import dimMoneyGroup
from database.DDL.dim_accountType import dimAccountType
from database.DDL.dim_account import dimAccount



if __name__ == '__main__':
    os.remove('database/moneyTracker.db')
    
    # See how to use data like [moneyGroup['name'] in html instead of by id
    # Highlight selected button
    
    print('hello')
    # Fact Movement - Setup
    factMovement = factMovement()
    factMovement.createTable()
    
    # Dim Date - Setup
    dimDate = dimDate()
    dimDate.createTable()
    
    # Dim Money Group - Setup
    dimMoneyGroup = dimMoneyGroup()
    dimMoneyGroup.createTable()
    moneyGroups = ['Car business', 'Tacos Zara', 'Garcan', 'Hersheys', 'Tech', 'Create money group']
    for moneyGroup in moneyGroups:
        dimMoneyGroup.insert(moneyGroupName=moneyGroup)
    
    # Dim Account Type - Setup
    dimAccountType = dimAccountType()
    dimAccountType.createTable()
    accountTypes = ['Credit', 'Debit', 'Investment', 'Payroll']
    for accountType in accountTypes:
        dimAccountType.insert(accountTypeName=accountType)
    
    # Dim Account - Setup
    dimAccount = dimAccount()
    dimAccount.createTable()
    accounts = [
        ['Banregio Debito', 1800, 1],
        ['HSBC Premier Nomina', 55000, 4],
        ['Banamex Nomina Ejecutiva', 35000, 4]
    ]
    for account in accounts:
        dimAccount.insert(
            accountName=account[0],
            accountBalance=account[1],
            accountTypeId=account[2]
        )
    
        
