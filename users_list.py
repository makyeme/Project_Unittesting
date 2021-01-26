import mysql.connector

##Connecting to database in mySQL
data_base = mysql.connector.connect( 
    
    host = "localhost", 
    user =  "makyeme",
    password = "xxxxxx",
    database = "my_database"
    )

my_cursor = data_base.cursor()


###Returning contents of the table "employee" from My_database

my_cursor.execute("SELECT * FROM employees")
row = my_cursor.fetchone()
while row is not None:
  print(row)
 
  row = my_cursor.fetchone()


