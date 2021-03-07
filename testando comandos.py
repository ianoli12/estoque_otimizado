from prettytable import PrettyTable

table = PrettyTable()
dados = [["ian"],["18"]]
columns = ["Famlia","Teste","teste2"]
cont = 0
table.field_names = columns

for x in range(len(dados)):
    #for y in range(len(columns)):
    table.add_row([dados[cont],dados[1]])
    
print(table)