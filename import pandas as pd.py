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
cursor = conn.cursor()

