import sqlite3

class factMovement:
    def __init__(self):
        self.conn = sqlite3.connect("database/moneyTracker.db")
        self.cur = self.conn.cursor()
        
        
        
    def runStatement(self, statement):
        self.cur.execute(statement)
        self.conn.commit()
        
        
    def createTable(self):
        createStatement = """
            CREATE TABLE IF NOT EXISTS FactMovements (
                Id INTEGER PRIMARY KEY,
                Amount INTEGER NOT NULL,
                Description TEXT,
                
                -- Foreign keys
                DateId INTEGER NOT NULL,
                TransactionTypeId INTEGER NOT NULL,
                AccountId INTEGER NOT NULL,
                MoneyGroupId INTEGER NOT NULL,
                
                FOREIGN KEY (DateId) REFERENCES DimDate (Id),
                FOREIGN KEY (TransactionTypeId) REFERENCES DimTransactionType (id),
                FOREIGN KEY (AccountId) REFERENCES DimAccount (id),
                FOREIGN KEY (MoneyGroupId) REFERENCES DimMoneyGroup (id)
            );
        """
        self.runStatement(createStatement)
        
        
    def insertMovement(self):
        insertStatement = f"""
            INSERT INTO FactMovements (
                Id,
                Amount,
                Description,
                DateId,
                TransactionTypeId,
                AccountId,
                MoneyGroupId
            ) VALUES (
                1,
                500,
                '05292023'
            ) ;
        """
        self.runStatement(insertStatement)
        


        
