import pyodbc
import os
import tableprint as tp
import numpy as np
from prettytable import PrettyTable
from tabulate import tabulate
import pandas as pd
import sqlalchemy as sa
import numpy as np

def modulo_est(conn):
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

        def modest_consprod(conn):
            pergunta = "s"
            
            while(pergunta == "s" and "S"):
                print("\nConsulta de Produtos:\n")
                #MOSTRA UM SIMPLES SELECT DA TABELA
                cursor = conn.cursor()
                #cursor.execute('SELECT TOP 10 PRODUCTID,NAME,PRODUCTNUMBER,COLOR,SAFETYSTOCKLEVEL,STANDARDCOST,LISTPRICE from Production.Product')
                #lista = list(cursor.execute('SELECT top 10 PRODUCTID,NAME from Production.Product'))
                df = pd.read_sql('SELECT top 10 PRODUCTID,NAME,PRODUCTNUMBER,Makeflag from Production.Product order by PRODUCTID',conn)
                print(df.to_string(index=False))

                #MOSTRA UM  SELECT APENAS DO CÓDIGO MENCIONADO
                CODPROD = int(input("Digite o código do produto: \n"))
                cursor.execute('select PRODUCTID from PRODUCTION.PRODUCT where PRODUCTID=?',CODPROD)
                
                prod_existe = 0
                
                #for x in df:
                #print(df.iloc[df[0],[0]].to_string(index=False))
                #if df['PRODUCTID'].values(CODPROD) == CODPROD:
                #print(np.where(df.index==CODPROD)[0])
                #df = productid.values[CODPROD]
                #print(df.values(1,[CODPROD])
                #if np.where(df.values([[1],[CODPROD]]):
                
                
                d = df["PRODUCTID"]
                #d = df.convert_dtypes(d)
                int(d)

                print(d.values([[1],[CODPROD]]))
                #df = pd.DataFrame()
                if df.values([CODPROD] == CODPROD):
                    print("Produto encontrado")
                    print(df.iloc[CODPROD])
                    prod_existe = 1                     
                else:
                    print("Produto não encontrado")
                    #print(df.iloc[CODPROD])
                pergunta = str(input("\nDeseja consultar novamente?(s/n)...\n"))

        def modest_addprod(conn): 
            pergunta = "s"
            while(pergunta == "s"):
                CODPROD = str(input("Insira o código do produto a ser incluído:\n"))
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

        def modest_delprod(conn):
            cursor = conn.cursor()
            cursor.execute(
            'delete from PRODUTOS where CODPROD = ?;',
            (2)
            )
            conn.commit()
            select_tab(conn)

        if op_moduloest == 1:
            modest_consprod(conn)
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

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-EK0ORPP;"
    "Database=AdventureWorks2017;"
    "Trusted_Connection=yes;"
)

print("BEM VINDO AO ESTOQUE BRASIL\n\n")

print("1 - Módulo de Estoque: \n")
print("2 - Sobre o software: \n")
op_menuprin = int(input('Digite a opção desejada:'))


if op_menuprin == 1:
    modulo_est(conn)
elif op_menuprin == 2:
    sobre_software()
else:
    print("Digite uma opção válida(numérica):")