import pandas as pd

data = [['New York Yankees ', '"Acevedo Juan"  ', 900000, ' Pitcher\n'], 
        ['New York Yankees ', '"Anderson Jason"', 300000, ' Pitcher\n'], 
        ['New York Yankees ', '"Clemens Roger" ', 10100000, ' Pitcher\n'], 
        ['New York Yankees ', '"Contreras Jose"', 5500000, ' Pitcher\n']]

data_transposed = zip(data)
df = pd.DataFrame(data_transposed, columns=["Team", "Player", "Salary", "Role"])