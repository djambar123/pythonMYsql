import mysql.connector

dani = mysql.connector.connect(
    host="localhost",
    user= 'root',
    password= 'dj4545801!',
    port= '3306',
    database= 'classicmodels'
)

mycursor = dani.cursor()
sql_Query = "select customerName,customerNumber from customers ORDER BY customerName"
mycursor.execute(sql_Query)
res = mycursor.fetchall()

for i in res:
    print(i)