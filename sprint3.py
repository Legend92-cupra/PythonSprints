import csv

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


# append_data("data_1.csv", "Nik-Naks", 26)
# append_data("data_1.csv", "Doritos", 35)
append_data("data_1.csv", "Pringles", 41)