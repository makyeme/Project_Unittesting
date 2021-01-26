import connectiondatabaserror
from connectiondatabaseerror import database_access

import unittest

from unittest.mock import patch

##Creating class TestDatabase
class TestDbError(Exception):
    
    ##Setting up two student users for the mock database
       def setUp(self):
          print('setUp')
          self.student_1 = ConnectionDatabaseError('localhost', 'makyeme', 'drip', 'my_database')
          self.student_2 = ConnectionDatabaseError('localhost', 'silver', 'sink', 'my_database')


    """Mocking te connection string to the original data base,
    thus creating a mock database"""
    
       def test_database_access(self):
        with patch('error_db.mysql.connector.connect') as mocked_connection:
            mocked_connection.return_value.ok = True
            mocked_connection.return_value.text = 'Success'


##testing mock database connection with student_1
            access = self.student_1.database_access(self)
            mocked_connection.assert_called_with(
                
                host = "localhost", 
                user =  "makyeme",
                password = "drip",
                database = "my_database"
           )
            self.assertEqual(access, 'Success')


####mocking failed connection due to wrong password by student_2
    mocked_connection.return_value.ok = False

            access = self.student_2.database_access(self)
            mocked_connection.assert_called_with(
                
                host = "localhost", 
                user =  "silver",
                password = "drip",
                database = "my_database"
           )
            self.assertEqual(access, 'connection failed')
