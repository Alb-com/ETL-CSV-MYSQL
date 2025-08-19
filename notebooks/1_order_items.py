#e_dataset_Comas_Albert
#contact = albertcomaas@gmail.com

import pandas as pd
import mysql.connector


df = pd.read_csv("order_items.csv")

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Albert22_",
    database = "e_dataset"
)

# Cursor is a element that allows use commands sql
cursor = connection.cursor()

# i used "_" cuz doesnt matter have a "index"
for _, row in df.iterrows():
    cursor.execute(
        """INSERT INTO order_items (item_id,order_id,product_id,quantity,unit_price)  
        VALUES (%s,%s,%s,%s,%s)""",
        (
            int(row['item_id']),
            row['order_id'],
            row['product_id'],
            row['quantity'],
            row['unit_price'],          
    )
        )

# to keep the data in permament format, not temporal
connection.commit()
# to close the conexion with data base
connection.close()

print(df)