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
    
    
    # Dim Date - Setup
    dimDate = dimDate()
    dimDate.createTable()
    
    
    # Dim Money Group - Setup
    dimMoneyGroup = dimMoneyGroup()
    dimMoneyGroup.createTable()
    
    moneyGroups = ['Car business', 'Tacos Zara', 'Garcan', 'Hersheys', 'Tech', 'Create money group']
    for moneyGroup in moneyGroups:
        dimMoneyGroup.insert(moneyGroup)
    
    
    # Dim Account Type - Setup
    dimAccountType = dimAccountType()
    dimAccountType.createTable()
    
    accountTypes = ['Credit', 'Debit', 'Investment', 'Payroll']
    for accountType in accountTypes:
        dimAccountType.insert(accountType)
    
    
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
    
    
    # Dim Transaction Type - Setup
    dimTransactionType = dimTransactionType()
    dimTransactionType.createTable()
    
    transactionTypeNames = ['Investment', 'Income', 'Expense', 'Transfer']
    for transactionTypeName in transactionTypeNames:
        dimTransactionType.insert(transactionTypeName)
    

    # Fact Movement - Setup
    factMovement = factMovement()
    factMovement.createTable()
    
    movements = [
        {
            'amount': 35500, 
            'description': 'Pago de nomina',
            'dateId': 20230530,
            'transactionTypeId': 2, 
            'accountId': 2, 
            'moneyGroupId': 5,
         },
        {
            'amount': 230000, 
            'description': 'Carro - Ford F150',
            'dateId': 20230413,
            'transactionTypeId': 1, 
            'accountId': 3, 
            'moneyGroupId': 1,
         },
        {
            'amount': 2000, 
            'description': 'Renta',
            'dateId': 20230630,
            'transactionTypeId': 3, 
            'accountId': 1, 
            'moneyGroupId': 2,
         },
    ]
    for movement in movements:
        factMovement.insert(**movement)
        
