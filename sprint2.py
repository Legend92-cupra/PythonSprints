import pandas as pd
import matplotlib.pyplot as plt

sample_data = pd.read_csv('data_1.csv')
# print(sample_data)

plt.bar(sample_data.Chips, sample_data.Availability)
plt.title('Chips_Table')
plt.xlabel('Brands')
plt.ylabel('Availability')
plt.show()


# Bar chart for Cooldrinks Table
sample_data = pd.read_csv('data_2.csv')
# print(sample_data)

plt.bar(sample_data.Cooldrinks, sample_data.Availability)
plt.title('Cooldrinks_Table')
plt.xlabel('Brands')
plt.ylabel('Availability')
plt.show()


# Bar chart for Chocolates Table
sample_data = pd.read_csv('data_3.csv')
# print(sample_data)

plt.bar(sample_data.Chocolates, sample_data.Availability)
plt.title('Chocolates_Table')
plt.xlabel('Brands')
plt.ylabel('Availability')
plt.show()


# Bar chart for Pies Table
sample_data = pd.read_csv('data_4.csv')
# print(sample_data)

plt.bar(sample_data.Pies, sample_data.Availability)
plt.title('Pies_Table')
plt.xlabel('Brands')
plt.ylabel('Availability')
plt.show()


# Bar chart for Fruit Table
sample_data = pd.read_csv('data_5.csv')
# print(sample_data)

plt.bar(sample_data.Fruit, sample_data.Availability)
plt.title('Fruits_Table')
plt.xlabel('Brands')
plt.ylabel('Availability')
plt.show()


# Bar chart for Cupcakes Table
sample_data = pd.read_csv('data_6.csv')
# print(sample_data)

plt.bar(sample_data.Cupcakes, sample_data.Availability)
plt.title('Cupcakes_Table')
plt.xlabel('Brands')
plt.ylabel('Availability')
plt.show()


# Bar chart for Veggies Table
sample_data = pd.read_csv('data_7.csv')
# print(sample_data)

plt.bar(sample_data.Veggies, sample_data.Availability)
plt.title('Vegetables_Table')
plt.xlabel('Brands')
plt.ylabel('Availability')
plt.show()