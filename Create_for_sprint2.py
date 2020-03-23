import pandas as pd

# Chips Table
raw_data_chips = {'Item_ID': ['1', '2'],
            'Chips': ['Simba', 'Lays'],
            'Availability': [25, 30]}

df = pd.DataFrame(raw_data_chips, columns=['Item_ID', 'Chips', 'Availability'])
df.to_csv('/Users/Eathan Coenraad/PycharmProjects/PythonSprintsCapaciti/data_1.csv',index=False)
print(df)


# Cooldrinks Table
raw_data_cooldrinks = {'Item_ID': ['1', '2'],
            'Cooldrinks': ['Coke', 'Fanta'],
            'Availability': [45, 21]}

df1 = pd.DataFrame(raw_data_cooldrinks, columns=['Item_ID', 'Cooldrinks', 'Availability'])
df1.to_csv('/Users/Eathan Coenraad/PycharmProjects/PythonSprintsCapaciti/data_2.csv',index=False)
print(df1)


# Chocolates Table
raw_data_chocolates = {'Item_ID': ['1', '2'],
            'Chocolates': ['Cadbury', 'Tex'],
            'Availability': [19, 10]}

df2 = pd.DataFrame(raw_data_chocolates, columns=['Item_ID', 'Chocolates', 'Availability'])
df2.to_csv('/Users/Eathan Coenraad/PycharmProjects/PythonSprintsCapaciti/data_3.csv',index=False)
print(df2)


# Pies Table
raw_data_pies = {'Item_ID': ['1', '2'],
            'Pies': ['Pepper Steak', 'Chicken'],
            'Availability': [25, 28]}

df3 = pd.DataFrame(raw_data_pies, columns=['Item_ID', 'Pies', 'Availability'])
df3.to_csv('/Users/Eathan Coenraad/PycharmProjects/PythonSprintsCapaciti/data_4.csv',index=False)
print(df3)


# Fruit Table
raw_data_fruit = {'Item_ID': ['1', '2', '3'],
            'Fruit': ['Pear', 'Apple', 'Orange'],
            'Availability': [50, 41, 32]}

df4 = pd.DataFrame(raw_data_fruit, columns=['Item_ID', 'Fruit', 'Availability'])
df4.to_csv('/Users/Eathan Coenraad/PycharmProjects/PythonSprintsCapaciti/data_5.csv',index=False)
print(df4)


# Cupcakes Table
raw_data_cupcakes = {'Item_ID': ['1', '2'],
            'Cupcakes': ['Vanilla', 'Chocolate'],
            'Availability': [31, 65]}

df5 = pd.DataFrame(raw_data_cupcakes, columns=['Item_ID', 'Cupcakes', 'Availability'])
df5.to_csv('/Users/Eathan Coenraad/PycharmProjects/PythonSprintsCapaciti/data_6.csv',index=False)
print(df5)


# Veggies Table
raw_data_veggies = {'Item_ID': ['1', '2'],
            'Veggies': ['Spinach', 'Cabbage'],
            'Availability': [13, 11]}

df6 = pd.DataFrame(raw_data_veggies, columns=['Item_ID', 'Veggies', 'Availability'])
df6.to_csv('/Users/Eathan Coenraad/PycharmProjects/PythonSprintsCapaciti/data_7.csv',index=False)
print(df6)