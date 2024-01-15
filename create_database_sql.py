import mysql.connector
try:
    conn = mysql.connector.connect(
        user = "userpython",
        host = "localhost",
        passwd = "123456"
    )
    mycursor =conn.cursor()
    mycursor.execute("CREATE DATABASE  mydatabasefrompython") 

except mysql.connector.Error as e:
    print(e)
        
