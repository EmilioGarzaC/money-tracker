import sqlite3

class dimAccount:
    def __init__(self):
        self.conn = sqlite3.connect("database/moneyTracker.db")
        self.cur = self.conn.cursor()
        
        
        
    def runStatement(self, statement):
        self.cur.execute(statement)
        self.conn.commit()
        
        
    def createTable(self):
        createStatement = """
            CREATE TABLE IF NOT EXISTS DimAccount (
                Id INTEGER PRIMARY KEY,
                Name VARCHAR(50),
                Balance INTEGER NOT NULL,
                AccountTypeId INTEGER NOT NULL,
                
                FOREIGN KEY (AccountTypeId) REFERENCES DimAccountType (Id)
            );
        """
        self.runStatement(createStatement)
        
        
    def insert(self, accountName, accountBalance, accountTypeId):
        insertStatement = f"""
            INSERT INTO DimAccount (
                Name, 
                Balance, 
                AccountTypeId) 
            VALUES (
                '{accountName}',
                {accountBalance},
                {accountTypeId}
            );
        """
        self.runStatement(insertStatement)
        
        
    def getAll(self):
        selectStatement = """
            SELECT * FROM DimAccount;
        """
        self.runStatement(selectStatement)
        return self.cur.fetchall()