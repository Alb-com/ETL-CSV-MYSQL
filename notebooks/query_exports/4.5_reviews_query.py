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
select * from reviews
where year(review_date) = 2025
order by rating desc;

"""

df = pd.read_sql(query, connection)
df.to_csv("query_reviews.csv", index=False)

connection.close()
