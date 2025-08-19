#e_dataset_Comas_Albert
#contact = albertcomaas@gmail.com

import pandas as pd
import mysql.connector

df = pd.read_csv("products.csv")

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Albert22_",
    database = "e_dataset"
)

# That allows use commands sql
cursor= connection.cursor()

# i used "_" cuz doesnt matter have a "index"
for _, row in df.iterrows():
    cursor.execute(
        """INSERT INTO products (product_id,name,category,price,in_stock)  
        VALUES (%s,%s,%s,%s,%s)""",
        (
            int(row['product_id']),
            row['name'],
            row['category'],
            row['price'],         
            row['in_stock'],         
    )
        )

# to keep the data in permament format, not temporal
connection.commit()
# to close the conexion with data base
connection.close()

print(df)