import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Eathan2704liezl",
    database="data_tracker",
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE data_table (Chips VARCHAR(255), Cooldrinks VARCHAR(255), Chocolates VARCHAR(255), Pies VARCHAR(255), Fruit VARCHAR(255), Cupcake VARCHAR(255), Veggies VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)

sqlFormula = "INSERT INTO data_table (Chips, Cooldrinks, Chocolates, Pies, Fruit, Cupcake, Veggies) VALUES (%s, %s, %s, %s, %s, %s, %s)"
Items = ("Simba", "Coke", "Cadbury", "Steak", "Apple", "Vanilla", "Spinach")
Items1 = ("Lays", "Fanta", "Tex", "Chicken", "Orange", "Chocolate", "Cabbage")

mycursor.execute(sqlFormula, Items)
mycursor.execute(sqlFormula, Items1)

mydb.commit()