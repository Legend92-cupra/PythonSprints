import pandas as pd

raw_data = {'Items': ['1', '2'],
            'Chips': ['Simba', 'Lays'],
            'Cooldrinks': ['Cooldrinks', 'Fanta'],
            'Chocolates': ['Cadbury', 'Tex'],
            'Pies': ['Pepper Steak', 'Chicken'],
            'Fruit': ['Pear', 'Apple'],
            'Cupcakes': ['Vanilla', 'Chocolate'],
            'Veggies': ['Spinach', 'Cabbage']}

df = pd.DataFrame(raw_data, columns=['Items', 'Chips', 'Cooldrinks', 'Chocolates', 'Pies', 'Fruit', 'Cupcakes', 'Veggies'])
df.to_csv('/Users/Eathan Coenraad/PycharmProjects/PythonSprintsCapaciti/data.csv',index=False)
print(df)
