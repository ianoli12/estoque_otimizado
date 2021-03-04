import pyodbc
import os
import tableprint as tp
import numpy as np
from prettytable import PrettyTable
from tabulate import tabulate
import pandas as pd
import sqlalchemy as sa
import MySQLdb
import prettytable
pt = PrettyTable()

"""engine = sa.create_engine('mssql://DESKTOP-EK0ORPP/AdventureWorks2017?trusted_connection=yes')
query = 'SELECT top 4 PRODUCTID,NAME from Production.Product'
df = pd.read_sql(query,engine)
print(df.head(4))"""

conn_mysqldb = MySQLdb.connect(host="127.0.0.1",port=3306,user="ianoli12",passwd="32244000",db="AdventureWorks")
df = pd.read_sql('SELECT PRODUCTID,NAME,PRODUCTNUMBER,COLOR,LISTPRICE,WEIGHT from Product',conn_mysqldb)
print(df.head(4))