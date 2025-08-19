#e_dataset_Comas_Albert
#contact = albertcomaas@gmail.com

import pandas as pd
import mysql.connector

df = pd.read_csv("orders.csv")

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
        """INSERT INTO orders (order_id,customer_id,order_date,total_amount)  
        VALUES (%s,%s,%s,%s)""",
        (
            int(row['order_id']),
            row['customer_id'],
            row['order_date'],
            row['total_amount'],         
    )
        )

# to keep the data in permament format, not temporal
connection.commit()
# to close the conexion with data base
connection.close()

print(df)
