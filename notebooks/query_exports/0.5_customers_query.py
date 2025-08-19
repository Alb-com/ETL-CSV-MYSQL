#e_dataset_Comas_Albert
#contact = albertcomaas@gmail.com

import pandas as pd
import mysql.connector

#conection
conection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Albert22_",
    database="e_dataset"
)

#query
query = "SELECT * FROM customers WHERE country = 'USA'"
df = pd.read_sql(query,conection)

#to keep it to csv
df.to_csv("query_customers.csv", index = False)

conection.close()