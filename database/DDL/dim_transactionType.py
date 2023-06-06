
import sqlite3

class dimTransactionType:
    def __init__(self):
        self.conn = sqlite3.connect("database/moneyTracker.db")
        self.cur = self.conn.cursor()
        
        
        
    def runStatement(self, statement):
        self.cur.execute(statement)
        self.conn.commit()
        
        
    def createTable(self):
        createStatement = """
            CREATE TABLE IF NOT EXISTS DimTransactionType  (
                Id INTEGER PRIMARY KEY,
                Name VARCHAR(50)
            );
        """
        self.runStatement(createStatement)
    
    
    def insert(self, transactionTypeName):
        insertStatement = f"""
            INSERT INTO DimTransactionType (Name) VALUES ('{transactionTypeName}')
        """
        self.runStatement(insertStatement)
            
            
    def getAll(self):
        selectStatement = """
            SELECT * FROM DimMoneyGroup;
        """
        self.runStatement(selectStatement)
        return self.cur.fetchall()