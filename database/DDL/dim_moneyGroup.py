
import sqlite3

class dimMoneyGroup:
    def __init__(self):
        self.conn = sqlite3.connect("database/moneyTracker.db")
        self.cur = self.conn.cursor()
        
        
        
    def runStatement(self, statement):
        self.cur.execute(statement)
        self.conn.commit()
        
        
    def createTable(self):
        createStatement = """
            CREATE TABLE IF NOT EXISTS DimMoneyGroup  (
                Id INTEGER PRIMARY KEY,
                Name VARDCHAR(50) UNIQUE NOT NULL
            );
        """
        self.runStatement(createStatement)
        
        
    def insert(self, moneyGroupName):
        insertStatement = f"""
            INSERT INTO DimMoneyGroup (Name) VALUES ('{moneyGroupName}');
        """
        self.runStatement(insertStatement)
            
            
    def getAll(self):
        selectStatement = """
            SELECT * FROM DimMoneyGroup;
        """
        self.runStatement(selectStatement)
        return self.cur.fetchall()