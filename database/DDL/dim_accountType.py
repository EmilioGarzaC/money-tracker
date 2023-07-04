
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
                Name VARCHAR(50) NOT NULL
            );
        """
        self.runStatement(createStatement)
        
        
    def insert(self, accountTypeName):
        insertStatement = f"""
            INSERT INTO DimAccountType (Name) VALUES ('{accountTypeName}');
        """
        self.runStatement(insertStatement)
        
        
    def getAll(self):
        selectStatement = """
            SELECT * FROM DimAccountType;
        """
        self.runStatement(selectStatement)
        return self.cur.fetchall()