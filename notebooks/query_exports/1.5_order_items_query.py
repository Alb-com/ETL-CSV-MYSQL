#e_dataset_Comas_Albert
#contact = albertcomaas@gmail.com

import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Albert22_",
    database = "e_dataset"
)

query = "select * from order_items where quantity > 2 AND unit_price < 500.00;"
df = pd.read_sql(query,connection)
df.to_csv("query_item_order.csv",index = False)

connection.close()

