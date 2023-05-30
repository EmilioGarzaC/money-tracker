
import sqlite3

class dimAccountType:
    def __init__(self):
        self.conn = sqlite3.connect("database/moneyTracker.db")
        self.cur = self.conn.cursor()
        
        
        
    def runStatement(self, statement):
        self.cur.execute(statement)
        self.conn.commit()
        
        
    def createTable(self):
        createStatement = """
            CREATE TABLE IF NOT EXISTS DimAccountType  (
                Id INTEGER PRIMARY KEY,
                Amount INTEGER NOT NULL,
                DateId TEXT NOT NULL,
                CategoryId INT NOT NULL,
                TransactionTypeId INT NOT NULL
            );
        """
        self.runStatement(createStatement)