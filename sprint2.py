import pandas as pd
import matplotlib.pyplot as plt

sample_data = pd.read_csv('data_1.csv')
# print(sample_data)

plt.bar(sample_data.Item_ID, sample_data.Availability)
plt.show()