#e_dataset_Comas_Albert
#contact = albertcomaas@gmail.com

import pandas as pd
import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Albert22_",
    database="e_dataset"
)


query = """
select * from products order by price desc

"""

df = pd.read_sql(query, connection)
df.to_csv("query_products.csv", index=False)

connection.close()
