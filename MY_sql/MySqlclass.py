import mysql.connector
class Mysql():
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user= 'root',
            password= 'dj4545801!',
            port= '3306',
            database= 'classicmodels')
        #self.a = con.cursor()

    def connectt(self,a,type):
        if type == 'select':
            str(a)
            mycursor = self.con.cursor()
            mycursor.execute(a)
            a = mycursor.fetchall()
            return  a
        else:
            self.con.commit()





