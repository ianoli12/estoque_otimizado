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


conn_mysqldb = MySQLdb.connect(host="127.0.0.1",port=3306,user="ianoli12",passwd="32244000",db="AdventureWorks")
df = pd.read_sql('SELECT PRODUCTID,NAME,PRODUCTNUMBER,COLOR,LISTPRICE,WEIGHT from Product',conn_mysqldb)
print("#####################################################################################")
print(df.head(4).to_string(index=False))
print("#####################################################################################")