import pyodbc
import os
import tableprint as tp
import numpy as np
from prettytable import PrettyTable
from tabulate import tabulate
import pandas as pd
import sqlalchemy as sa
import numpy as np
import functools
from datetime import date
from termcolor import colored


def modulo_est(conn):
    verficador = 2
    while(verficador == 2):
        print(colored("\n__________ MÓDULOS DE ESTOQUE __________\n","blue"))

        print("1 - Consultar Produto do Estoque:\n")
        print("2 - Adicionar Produto ao Estoque:\n")
        print("3 - Alterar Produto do Estoque\n")
        print("4 - Excluir Produto\n")
        print("5 - Sair\n")
        op_moduloest = int(input("Digite a opção desejada> "))

        # CONSULTANDO PRODUTOS
        def modest_consprod(conn):
            pergunta = "s"
            
            while(pergunta == "s" and "S"):
                print("\nConsulta de Produtos:\n")
                cursor = conn.cursor()
                df = pd.read_sql('SELECT TOP 10 PRODUCTID,NAME,PRODUCTNUMBER,Makeflag from Production.Product order by PRODUCTID',conn)
                print(colored(df.to_string(index=False),"blue"))

                CODPROD = int(input("Digite o código do produto: \n"))
                cursor.execute('select PRODUCTID from PRODUCTION.PRODUCT where PRODUCTID=?',CODPROD)
                
                prod_existe = 0
                res = 0
                for x in cursor:
                    res = int(''.join(map(str,x)))

                if res == CODPROD:
                    print("Dados do Produto:\n")
                    print(df.loc[df['PRODUCTID']==res,['PRODUCTID','NAME','PRODUCTNUMBER','Makeflag']].to_string(index=False))
                else:
                    print("Produto não encontrado")
                pergunta = str(input("\nDeseja consultar novamente?(s/n)...\n"))

        # ADICIONANDO PRODUTOS
        def modest_addprod(conn):
            pergunta = "s"
            cursor = conn.cursor()
            while(pergunta == "s" and "S"):
                prod_igual = ""
                df2 = 0
                res = 0
                
                for x in cursor:
                    res = int(''.join(map(str,x)))

                while(prod_igual == ""):
                    PRODUCTID = int(input("\nDigite o código do produto a ser incluído: \n"))
                    if PRODUCTID == df2.loc[df2['ProductID']==PRODUCTID,['ProductID']].to_string(index=False):
                        print(colored("O Código deste produto já está cadastrado","red"))
                        prod_igual = ""

                NAME = str(input("\n Novo nome: \n"))
                PRODUCTNUMBER = str(input("\nNova Identificação do Produto(ProductNumer): \n"))
                MAKEFLAG = bool(input("\nDigite a MakeFlag do Produto: \n"))
                FINISHEDGOODSFLAG = bool(input("\nDigite a FINISHEDGOODSFLAG do produto: \n"))
                COLOR = str(input("\n Cor do Produto: \n"))
                SAFETYSTOCKLEVEL = int(input("\nDigite a quantidade segura de estoque: \n"))
                REORDERPOINT = int(input("\nDigite o ponto de reordenação do produto: \n"))
                STANDARDCOST = float(input("\nDigite o preço padrão: \n"))
                LISTPRICE = float(input("\nDigite o valor na lista de preço desse produto: \n"))
                DAYSTOMANUFACTURE = int(input("\nQuantidade de dias para a manufatura do produto: \n"))
                SELLSTARTDATE = str(input("\n Digite a Data Inicial de venda do produto: (Ex:2008-04-30): \n"))

                cursor = conn.cursor()
                cursor.execute('SET IDENTITY_INSERT [Production].[Product] ON;INSERT INTO Production.Product(ProductID,Name,ProductNumber,MakeFlag,FinishedGoodsFlag,Color,SafetyStockLevel,ReorderPoint,StandardCost,ListPrice,DaysToManufacture,SellStartDate) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',PRODUCTID,NAME,PRODUCTNUMBER,MAKEFLAG,FINISHEDGOODSFLAG,COLOR,SAFETYSTOCKLEVEL,REORDERPOINT,STANDARDCOST,LISTPRICE,DAYSTOMANUFACTURE,SELLSTARTDATE)
                conn.commit()
                df2 = pd.read_sql('SELECT ProductID,Name,ProductNumber,MakeFlag,FinishedGoodsFlag,Color,SafetyStockLevel,ReorderPoint,StandardCost,ListPrice,DaysToManufacture,SellStartDate FROM PRODUCTION.PRODUCT ORDER BY PRODUCTID',conn)
                print(colored(df2.loc[df2['ProductID']==PRODUCTID,['ProductID','Name','ProductNumber','MakeFlag','FinishedGoodsFlag','Color','SafetyStockLevel','ReorderPoint','StandardCost','ListPrice','DaysToManufacture','SellStartDate']].to_string(index=False),"blue"))

                pergunta = str(input("\nDeseja INCLUIR o produto novamente?...\n"))

        # ALTERANDO PRODUTOS
        def modest_altprod(conn): 
            print("\Alteração de Produtos:\n")
            pergunta = "s"
            while(pergunta == "s" and "S"):                
                df = pd.read_sql('SELECT TOP 10 ProductID,Name,ProductNumber,MakeFlag,FinishedGoodsFlag,Color,SafetyStockLevel,ReorderPoint,StandardCost,ListPrice,DaysToManufacture,SellStartDate FROM Production.Product',conn)
                print(df.to_string(index=False))

                PRODUCTID = int(input("\nDigite o código do produto a ser alterado: \n"))
                cursor = conn.cursor()
                cursor.execute('select PRODUCTID from PRODUCTION.PRODUCT where PRODUCTID=?',PRODUCTID)
                res = 0
                for x in cursor:
                    res = int(''.join(map(str,x)))
                    print(res)

                if res == PRODUCTID:
                    print("Dados do Produto:\n")
                    print(df.loc[df['ProductID']==res,['ProductID','Name','ProductNumber','MakeFlag']].to_string(index=False))
                else:
                    print("Produto não encontrado")
                print("Preencha os valores a serem alterados\n")

                NAME = str(input("\n Novo nome: \n"))
                PRODUCTNUMBER = str(input("\nNova Identificação do Produto(ProductNumer): \n"))
                MAKEFLAG = bool(input("\nNovo MakeFlag do Produto: \n"))
                FINISHEDGOODSFLAG = bool(input("\nNovo FINISHEDGOODSFLAG do produto: \n"))
                COLOR = str(input("\n Nova Cor do Produto: \n"))
                SAFETYSTOCKLEVEL = int(input("\nNova quantidade segura de estoque: \n"))
                REORDERPOINT = int(input("\nNovo ponto de reordenação do produto: \n"))
                STANDARDCOST = float(input("\nNovo preço padrão: \n"))
                LISTPRICE = float(input("\nNovo valor na lista de preço desse produto: \n"))
                DAYSTOMANUFACTURE = int(input("\nNova quantidade de dias para a manufatura do produto: \n"))
                SELLSTARTDATE = str(input("\n Nova Data Inicial de venda do produto: (Ex:2008-04-30): \n"))

                cursor = conn.cursor()       
                cursor.execute('SET IDENTITY_INSERT [Production].[Product] ON;UPDATE Production.Product SET Name=?,ProductNumber=?,MakeFlag=?,FinishedGoodsFlag=?,Color=?,SafetyStockLevel=?,ReorderPoint=?,StandardCost=?,ListPrice=?,DaysToManufacture=?,SellStartDate=? WHERE ProductID = ?',NAME,PRODUCTNUMBER,MAKEFLAG,FINISHEDGOODSFLAG,COLOR,SAFETYSTOCKLEVEL,REORDERPOINT,STANDARDCOST,LISTPRICE,DAYSTOMANUFACTURE,SELLSTARTDATE,PRODUCTID)
                conn.commit()
                pergunta = str(input("\nDeseja ALTERAR o produto novamente?...\n"))     

        # DELETANDO PRODUTOS
        def modest_delprod(conn):

            print("\Remover Produtos:\n")
            pergunta = "s"
            while(pergunta == "s" and "S"):                
                df = pd.read_sql('SELECT TOP 10 ProductID,Name,ProductNumber,MakeFlag,FinishedGoodsFlag,Color,SafetyStockLevel,ReorderPoint,StandardCost,ListPrice,DaysToManufacture,SellStartDate FROM Production.Product',conn)
                print(df.to_string(index=False))

                PRODUCTID = int(input("\nDigite o código do produto a ser excluído: \n"))
                cursor = conn.cursor()
                cursor.execute('select PRODUCTID from PRODUCTION.PRODUCT where PRODUCTID=?',PRODUCTID)
                res = 0
                for x in cursor:
                    res = int(''.join(map(str,x)))
                    print(res)

                if res == PRODUCTID:
                    print(colored("Deseja REALMENTE excluir o Produto:\n","red"))
                    escolha = str(input("(Sim ou Não) S ou N: \n"))
                    if escolha == 's' or 'S':
                        cursor.execute('SET IDENTITY_INSERT [Production].[Product] ON;DELETE FROM Production.Product WHERE ProductID = ?',PRODUCTID)
                        conn.commit()
                        print("Produto Deletado")
                else:
                    print("Produto não encontrado")
                pergunta = str(input("\nDeseja EXCLUIR outro produto?...\n"))

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

# SOBRE O SOFTWARE
def sobre_software():
    print("Este software foi produzido por Ian Oliveira")

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-EK0ORPP;"
    "Database=AdventureWorks2017;"
    "Trusted_Connection=yes;"
)

# MENU PRINCIPAL
print(colored("\n\n\n\n\n\n---- [ BEM VINDO AO ESTOQUE OTIMIZADO ] ----\n\n",'green'))

print("1 - Módulo de Estoque: \n")
print("2 - Sobre o software: \n")
op_menuprin = int(input('Digite a opção desejada > '))


if op_menuprin == 1:
    modulo_est(conn)
elif op_menuprin == 2:
    sobre_software()
else:
    print("Digite uma opção válida(numérica): \n")


