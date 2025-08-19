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
SELECT 
    customer_id,
    SUM(total_amount) AS total_gastado,
    COUNT(order_id) AS numero_pedidos
FROM orders
WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY customer_id
ORDER BY total_gastado DESC;
"""

df = pd.read_sql(query, connection)
df.to_csv("query_orders.csv", index=False)

connection.close()
