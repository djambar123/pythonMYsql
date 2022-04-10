import mysql.connector
class Mysql:
    def connect(self):
        dani = mysql.connector.connect(
            host="localhost",
            user= 'root',
            password= 'dj4545801!',
            port= '3306',
            database= 'classicmodels'
        )

mycursor = mysql.connect()
sql_Query = "select customerName,customerNumber from customers ORDER BY customerName"
mycursor.execute(sql_Query)
res = mycursor.fetchall()

for i in res:
    print(i)