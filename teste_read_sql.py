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
import pymysql
from sqlalchemy import create_engine


conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-EK0ORPP;"
    "Database=EstoquePython;"
    "Trusted_Connection=yes;"
)
"""conn = pymysql.connect(host='localhost',
                             user='root',
                             password='ianoli12',
                             db='employee')"""

"""engine = create_engine('mysql+mysqldb://root:ianoli12@localhost:3306/estoque')
"""

#conn_mysqldb = 'mysql+pymysql://root:ianoli12@localhost:3306/AdventureWorks?charset=utf8mb4'
#conn_mysqldb = 'mysql+pymysql://root:ianoli12@localhost:3306/AdventureWorks?charset=utf8'
#conn_mysqldb = MySQLdb.connect(user='ianoli12',passwd='32244000',db='AdventureWorks')
#conn_mysqldb = 'mysql+mysqldb://root:ianoli12@localhost:3306/AdventureWorks'
#conn_mysqldb = MySQLdb.connect(host="127.0.0.1",port=3306,user="ianoli12",passwd="32244000",db="AdventureWorks")

#df_productid = pd.read_sql('insert into PRODUTOS values(?,?,?,?)',CODPROD,DESCPROD,QUANTPROD,STATUSPROD,conn_mysqldb)


#df = pd.read_sql_query("SELECt CODPROD,DESCPROD,QUANTPROD,STATUSPROD from PRODUTOS",engine)



#df.to_sql("INSERT INTO PRODUTOS VALUES (5,'TAMPA',10,1)",engine)


"""df = pd.to_sql("INSERT INTO PRODUTOS VALUES (5,'TAMPA',10,1)",engine)
"""
cursor=conn.cursor()


"""CODPROD = str(input("Insira o código do produto a ser incluído:\n"))
DESCPROD = str(input("Insira a descrição do produto:\n"))
QUANTPROD = float(input("Insira a quantidade do produto:\n"))
STATUSPROD = bool(input("Insira o status do produto:\n"))"""

"""sql = "INSERT INTO PRODUTOS VALUES(?,?,?,?)"
print(sql)
cursor.execute(sql,(6,'TAMPA',10,1))"""

conn.commit()
sql = "SELECT * FROM PRODUTOS"
cursor.execute(sql)
#result = cursor.fetchall()

i = []
for linha in cursor:
    i.append([elem for elem in linha])

df = pd.DataFrame(i)
df = df.transpose()
"""df = pd.DataFrame(sql)"""

print(df.head())
#print(df.head(20).to_string(index=False))