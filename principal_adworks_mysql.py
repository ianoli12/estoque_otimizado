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



conn_mysqldb = 'mysql://root:ianoli12@localhost:3306/AdventureWorks'
#conn_mysqldb = 'mysql+pymysql://root:ianoli12@localhost:3306/AdventureWorks?charset=utf8'
#conn_mysqldb = MySQLdb.connect(user='ianoli12',passwd='32244000',db='AdventureWorks')
#conn_mysqldb = 'mysql+mysqldb://root:ianoli12@localhost:3306/AdventureWorks'


#conn_mysqldb = MySQLdb.connect(host="127.0.0.1",port=3306,user="ianoli12",passwd="32244000",db="AdventureWorks")
#df = pd.read_sql('SELECT PRODUCTID,NAME,PRODUCTNUMBER,COLOR,LISTPRICE,WEIGHT from Product',conn_mysqldb)
"""print("#####################################################################################")
print(df.head(4).to_string(index=False))
print("#####################################################################################")
"""

def modulo_est(conn_mysqldb):
    verficador = 2
    while(verficador == 2):
        print("\nMÓDULO DE ESTOQUE\n")

        print("1 - Consultar Produto do Estoque:\n")
        print("2 - Adicionar Produto ao Estoque:\n")
        print("3 - Alterar Produto do Estoque\n")
        print("4 - Excluir Produto\n")
        print("5 - Sair\n")
        op_moduloest = int(input("Digite a opção desejada\n"))

        #FAZ SELECT SIMPLES 
        #def select_tab(conn):
         #    cursor = conn.cursor()
          #   cursor.execute('select * from PRODUTOS')


        def modest_consprod(conn_mysqldb):
            pergunta = "s"
            
            while(pergunta == "s" and "S"):
                print("\nConsulta de Produtos:\n")
                #MOSTRA UM SIMPLES SELECT DA TABELA
                df = pd.read_sql('SELECT PRODUCTID,NAME,PRODUCTNUMBER,COLOR,LISTPRICE,WEIGHT from Product',conn_mysqldb)
                print(df.head(4).to_string(index=False))

                #MOSTRA UM  SELECT APENAS DO CÓDIGO MENCIONADO
                PRODUCTID = str(input("Digite o código do produto: \n"))
                df_productid = pd.read_sql('select PRODUCTID from PRODUCTS where PRODUCTID=?',PRODUCTID,conn_mysqldb,params=list)
                prod_existe = 0
                """for x in cursor:                
                    print("|",x[0],"|",x[1],"|",x[2],"|",x[3],"|")"""

                if df_productid == PRODUCTID:
                    prod_existe = 1                     
                print()
                if prod_existe != 1:
                    print("Produto não encontrado")
                pergunta = str(input("\nDeseja consultar novamente?(s/n)...\n"))

        def modest_addprod(conn): 
            pergunta = "s"
            while(pergunta == "s"):
                PRODUCTID = str(input("Insira o código do produto a ser incluído:\n"))
                DESCPROD = str(input("Insira a descrição do produto:\n"))
                QUANTPROD = float(input("Insira a quantidade do produto:\n"))
                STATUSPROD = bool(input("Insira o status do produto:\n"))
                
                cursor = conn.cursor()
                cursor.execute(
                'insert into PRODUTOS values(?,?,?,?)',CODPROD,DESCPROD,QUANTPROD,STATUSPROD)
                conn.commit()
                pergunta = str(input("\nDeseja inserir outro produto novamente?(s/n)...\n"))

        def modest_altprod(conn):
            pergunta = "s"
            while(pergunta == "s"):
                CODPROD = str(input("\nDigite o código do produto a ser alterado: \n"))
                ALT_CODPROD = str(input("\n Novo código: \n"))
                ALT_DESCPROD = str(input("\nNova descrição: \n"))
                ALT_QUANTPROD = float(input("\nNova quantidade: \n"))
                ALT_STATUSPROD = bool(input("\nNovo status: \n"))
                

                cursor = conn.cursor()
                cursor.execute(
                'UPDATE PRODUTOS SET CODPROD=?,DESCPROD=?,QUANTPROD=?,STATUSPROD=? WHERE CODPROD='+CODPROD+' ',ALT_CODPROD,ALT_DESCPROD,ALT_QUANTPROD,ALT_STATUSPROD)
                conn.commit()
                pergunta = str(input("\nDeseja alterar o produto novamente?...\n"))

        def modest_delprod(conn_mysqldb):
            cursor = conn.cursor()
            cursor.execute(
            'delete from PRODUTOS where CODPROD = ?;',
            (2)
            )
            conn.commit()
            select_tab(conn)

        if op_moduloest == 1:
            modest_consprod(conn_mysqldb)
        elif op_moduloest == 2:
            modest_addprod(conn)
        elif op_moduloest == 3:
            modest_altprod(conn)
        elif op_moduloest == 4:
            modest_delprod(conn)
        else:
            print("A opção precisa ser numérica")


def sobre_software():
    print("Este software foi produzido por Ian Oliveira")


print("BEM VINDO AO ESTOQUE BRASIL\n\n")

print("1 - Módulo de Estoque: \n")
print("2 - Sobre o software: \n")
op_menuprin = int(input('Digite a opção desejada:'))


if op_menuprin == 1:
    modulo_est(conn_mysqldb)
elif op_menuprin == 2:
    sobre_software()
else:
    print("Digite uma opção válida(numérica):")