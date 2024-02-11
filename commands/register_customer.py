from models.user import User
from core.application_data import ApplicationData
class RegisterCustomer():
    def __init__(self, params, app_data: ApplicationData):
        self._app_data = app_data
        self._params = params

    def execute(self):
        first_name, last_name, username, email = self._params
        new_user = User(first_name, last_name, username, email)
        self._app_data.add_user(new_user)
        return f"User {new_user.first_name} {new_user.last_name} registered successfully."