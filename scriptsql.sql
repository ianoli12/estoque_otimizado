use AdventureWorks2017

SELECT * FROM Production.Product
SELECT TOP 10 * FROM Production.Product order by name



SET IDENTITY_INSERT [Production].[Product] ON;

INSERT INTO Production.Product(ProductID,Name,ProductNumber,MakeFlag,FinishedGoodsFlag,Color,SafetyStockLevel,ReorderPoint,StandardCost,ListPrice,DaysToManufacture,SellStartDate)
     VALUES
           (1000,'lampada','atr',1,1,'Silver',100,75,30082179,564,1,2008-04-30)





PRODUCTID,NAME,PRODUCTNUMBER,MAKEFLAG,FINISHEDGOODSFLAG,COLOR,SAFETYSTOCKLEVEL,REORDERPOINT,STANDARDCOST,LISTPRICE,DAYSTOMANUFACTURE,SELLSTARTDATE
SELECT ProductID,Name,ProductNumber,MakeFlag,FinishedGoodsFlag,Color,SafetyStockLevel,ReorderPoint,StandardCost,ListPrice,DaysToManufacture,SellStartDate FROM PRODUCTION.PRODUCT ORDER BY ProductID DESC

DELETE FROM Production.Product WHERE ProductID BETWEEN 1000 AND 1034

DELETE FROM Production.Product WHERE ProductID = 300


SELECT TOP 10 ProductID,Name,ProductNumber,MakeFlag,FinishedGoodsFlag,Color,SafetyStockLevel,ReorderPoint,StandardCost,ListPrice,DaysToManufacture,SellStartDate FROM PRODUCTION.PRODUCT ORDER BY ProductID DESC

UPDATE Production.Product SET ProductID,Name,ProductNumber,MakeFlag,FinishedGoodsFlag,Color,SafetyStockLevel=?,ReorderPoint=?,StandardCost=?,ListPrice=?,DaysToManufacture=?,SellStartDate=? WHERE ProductID = ?