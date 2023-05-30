from database.DDL.fact_movement import factMovement
from database.DDL.dim_date import dimDate

if __name__ == '__main__':
    print('hello')
    factMovement = factMovement()
    factMovement.createTable()
    #factMovement.insertTestData()
    
    dimDate = dimDate()
    dimDate.createTable()
