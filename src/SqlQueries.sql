-- SQLite
-- SELECT *
-- FROM FactMovements;

-- SELECT *
-- FROM DimDate
-- WHERE Id = '20230530'; 

-- SELECT * 
-- FROM DimAccount da
-- JOIN DimAccountType dat ON da.AccountTypeId = dat.Id;

-- SELECT * 
-- FROM DimMoneyGroup;

SELECT *
FROM FactMovements fm
JOIN DimTransactionType dtt ON dtt.Id = fm.TransactionTypeId
JOIN DimDate dd ON dd.Id = fm.DateId
JOIN DimAccount da ON da.Id = fm.AccountId
JOIN DimMoneyGroup dmg ON dmg.Id = fm.MoneyGroupId