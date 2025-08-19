#e_dataset_Comas_Albert
#contact = albertcomaas@gmail.com

import pandas as pd
import mysql.connector

df = pd.read_csv("customers.csv")

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
        """INSERT INTO customers (customer_id,name,email,country,registration_date)  
        VALUES (%s,%s,%s,%s,%s)""",
        (
            int(row['customer_id']),
            row['name'],
            row['email'],
            row['country'],
            row['registration_date'],          
    )
        )

# to keep the data in permament format, not temporal
connection.commit()
# to close the conexion with data base
connection.close()

print(df)

