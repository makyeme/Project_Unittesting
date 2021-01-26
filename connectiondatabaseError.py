import mysql.connector


#creating class "ConnectionDatabaseError" inheriting from the object exeception

class ConnectionDatabaseError(Exception):

    ###Creating instant atrributes to be used later in mock database
    def __init__(self, host, user, password, database):
        
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
    

    #method to raise error when connection to database fails
    
    def database_access(self):
      
       ##connection string to database 
        connection = mysql.connector.connect(
            f'host = {self.host}, user =  {self.user}, password = {self.password}, database = {self.database}'
            )


        if connection.ok:
            return connection.text
        else:
            return 'connection failed'
        
        
      
        
      
    
 