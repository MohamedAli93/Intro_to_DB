import mysql.connector
try:
    mydb = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "",
        )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store" )
    mydb.commit()
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as err:
    print(f"Error creating database: {err}")
finally:
    if mycursor:
      mycursor.close()
    if mydb:
      mydb.close()        