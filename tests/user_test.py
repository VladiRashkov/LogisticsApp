import unittest
from models.user import User

class User_Should(unittest.TestCase):
    def test_assign_values(self):
        #Arrange & Act
        test_user = User('Fernando', 'Alonso', 'fernso14', 'fernando_alonso@gmail.com')
        #Assert
        self.assertEqual('Fernando', test_user.first_name)
        self.assertEqual('Alonso', test_user.last_name)
        self.assertEqual('fernso14', test_user.username)
        self.assertEqual('fernando_alonso@gmail.com', test_user.email)

    def test_UserEmail_raises_ValueError_when_invalid_email(self):
        #Arrange & Act & Assert
        with self.assertRaises(ValueError):
            test_user = User('Fernando', 'Alonso', 'fernso14', 'invalidemail.com')


    def test_str_should_format_correctly(self):
        #Arrange
        expected_output = ' Fernando, \n Alonso, \n fernso14, \n fernando_alonso@gmail.com'
        
        test_user = User('Fernando', 'Alonso', 'fernso14', 'fernando_alonso@gmail.com')

        #Assert
        self.assertEqual(expected_output, str(test_user))