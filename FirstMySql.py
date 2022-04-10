import mysql.connector
dani = mysql.connector.connect(
    host="localhost",
    user= 'root',
    password= 'dj4545801!',
    port= '3306',
    database= 'classicmodels'
)
sql_select_Query = "select custumerName from customer"
cursor = dani.cursor()
cursor.execute(sql_select_Query)