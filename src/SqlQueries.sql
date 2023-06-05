-- SQLite
SELECT *
FROM FactMovements;

SELECT *
FROM DimDate
WHERE Id = '20230530'; 

SELECT * 
FROM DimAccount da
JOIN DimAccountType dat ON da.AccountTypeId = dat.Id;

SELECT * 
FROM DimMoneyGroup;