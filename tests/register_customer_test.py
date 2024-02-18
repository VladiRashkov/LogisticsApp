from models.user import User
from core.application_data import ApplicationData
from commands.register_customer import RegisterCustomer
import unittest

class RegisterUser_Should(unittest.TestCase):
    def test_execute(self):
        app_data = ApplicationData()

        params = ["John", "Scully", "jscully", "jscully@gmicl.com" ]

        command = RegisterCustomer(params, app_data)

        result = command.execute()
        
        user = app_data.users[0]

        self.assertEqual(len(app_data.users), 1)

        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Scully")
        self.assertEqual(user.username, "jscully")
        self.assertEqual(user.email, "jscully@gmicl.com")
        
        
        expected_result = "User John Scully registered successfully."
        self.assertEqual(result, expected_result)

    