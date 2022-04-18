from MySqlclass import Mysql

class Main_Qurey1(Mysql):
        mycursor1 = Mysql().connectt("select contactFirstName from customers","select")
        print(mycursor1)

        # update1 = Mysql().connectt("UPDATE customers SET contactFirstName ='daniel'  WHERE contactFirstName = 'Jean'")
        # print(update1)

        update2 = Mysql().connectt("UPDATE customers SET contactFirstName ='daniel'  WHERE contactFirstName = 'Jambar'","update")
        print(update2)

        mycursor2 = Mysql().connectt("select contactFirstName from customers WHERE contactFirstName = 'Miguel'",'select')
        print(mycursor2)

        mycursor4 = Mysql().connectt("select contactLastName from customers WHERE contactFirstName = 'JAMBAR'","select")
        print(mycursor4)


        countName = Mysql().connectt("SELECT COUNT(customerName) AS NumberOfcustomer FROM customers ","select")
        print(countName)



