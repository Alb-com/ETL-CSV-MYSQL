#e_dataset_Comas_Albert
#contact = albertcomaas@gmail.com

import pandas as pd
import mysql.connector

df = pd.read_csv("reviews.csv")

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
        """INSERT INTO reviews (review_id,product_id,customer_id,rating,review_date,comment)  
        VALUES (%s,%s,%s,%s,%s,%s)""",
        (
            int(row['review_id']),
            row['product_id'],
            row['customer_id'],
            row['rating'],         
            row['review_date'],        
            row['comment'],        
    )
        )

# to keep the data in permament format, not temporal
connection.commit()
# to close the conexion with data base
connection.close()

print(df)