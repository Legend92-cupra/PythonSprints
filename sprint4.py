import pandas as pd
import csv


# Sort Data by column name 'Chips' in descending order
data = pd.read_csv('data_1.csv')
dataset = pd.DataFrame(data, columns=['Item_ID', 'Chips', 'Availability'])
sort_data = dataset.sort_values(by='Availability', ascending=False)


# Drop row with Availability greater or equal to 30 units
# drop_func = sort_data.drop(sort_data[sort_data['Availability'] >= 30].index, inplace=True)



# The 'head()' function will automatically view the top 5 rows in a database
# The 'tail()' function will automatically view the bottom 5 rows in a database
top_data = sort_data.head()
bottom_data = sort_data.tail()


def get_length(file_path):
    with open("data_1.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        # print(reader_list)
        return len(reader_list)

def append_data(file_path, chips, availability):
    fieldnames = ['Item_ID', 'Chips', 'Availability']
    next_id = get_length(file_path)
    with open(file_path, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"Item_ID": next_id, "Chips": chips, "Availability": availability})


# append_data("data_1.csv", "Jumpy-Jacks", 14)
# append_data("data_1.csv", "Cheese-Naks", 9)
# append_data("data_1.csv", "Cheetos", 13)
# append_data("data_1.csv", "Fritos", 32)
# append_data("data_1.csv", "BigCorn Bites", 19)

print(sort_data)
print("Top 5 wanted brands")
print(top_data)
print("Bottom 5 least wanted brands")
print(bottom_data)
