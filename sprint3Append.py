import csv


# Append data to Chips Table
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
# append_data("data_1.csv", "Pringles", 41)


# Append data to Cooldrinks Table
def get_length(file_path):
    with open("data_2.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        # print(reader_list)
        return len(reader_list)

def append_data(file_path, cooldrink, availability):
    fieldnames = ['Item_ID', 'Cooldrinks', 'Availability']
    next_id = get_length(file_path)
    with open(file_path, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"Item_ID": next_id, "Cooldrinks": cooldrink, "Availability": availability})


# append_data("data_2.csv", "Sprite", 34)
# append_data("data_2.csv", "Jive", 45)
# append_data("data_2.csv", "7 Up", 22)


# Append data to Chocolates Table
def get_length_choc(file_path):
    with open("data_3.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        # print(reader_list)
        return len(reader_list)

def append_data(file_path, chocolate, availability):
    fieldnames = ['Item_ID', 'Chocolates', 'Availability']
    next_id = get_length_choc(file_path)
    with open(file_path, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"Item_ID": next_id, "Chocolates": chocolate, "Availability": availability})


# append_data("data_3.csv", "TV Bar", 34)
# append_data("data_3.csv", "Bar One", 39)
# append_data("data_3.csv", "Lindt", 20)


# Append data to Pies Table
def get_length_pies(file_path):
    with open("data_4.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        # print(reader_list)
        return len(reader_list)

def append_data(file_path, pies, availability):
    fieldnames = ['Item_ID', 'Pies', 'Availability']
    next_id = get_length_pies(file_path)
    with open(file_path, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"Item_ID": next_id, "Pies": pies, "Availability": availability})


append_data("data_4.csv", "Steak", 13)
append_data("data_4.csv", "Mutton Curry", 24)
append_data("data_4.csv", "Burger", 23)


# Append data to Fruit Table
def get_length_fruit(file_path):
    with open("data_5.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        # print(reader_list)
        return len(reader_list)

def append_data(file_path, fruit, availability):
    fieldnames = ['Item_ID', 'Fruit', 'Availability']
    next_id = get_length_fruit(file_path)
    with open(file_path, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"Item_ID": next_id, "Fruit": fruit, "Availability": availability})


append_data("data_5.csv", "Banana", 31)
append_data("data_5.csv", "Strawberries", 45)
append_data("data_5.csv", "Lemons", 10)


# Append data for Cupcakes Table
def get_length_cake(file_path):
    with open("data_6.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        # print(reader_list)
        return len(reader_list)

def append_data(file_path, cake, availability):
    fieldnames = ['Item_ID', 'Cupcakes', 'Availability']
    next_id = get_length_cake(file_path)
    with open(file_path, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"Item_ID": next_id, "Cupcakes": cake, "Availability": availability})


append_data("data_6.csv", "Banana", 12)
append_data("data_6.csv", "Red Velvet", 23)
append_data("data_6.csv", "Carrot", 18)


# Append data for Veggies Table
def get_length_veg(file_path):
    with open("data_7.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        # print(reader_list)
        return len(reader_list)

def append_data(file_path, veg, availability):
    fieldnames = ['Item_ID', 'Veggies', 'Availability']
    next_id = get_length_veg(file_path)
    with open(file_path, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"Item_ID": next_id, "Veggies": veg, "Availability": availability})


append_data("data_7.csv", "Lettuce", 6)
append_data("data_7.csv", "Broccoli", 13)
append_data("data_7.csv", "Carrots", 14)