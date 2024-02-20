import unittest
from commands.create_route import CreateRouteCommand
from core.application_data import ApplicationData

class CreateRoute_Should(unittest.TestCase):

    def test_execute_adds_route_successfully(self):
        #Arrange
        app_data = ApplicationData()
        start_loc = 'AliceSprings'
        other_loc = 'Adelaide' 'Melbourne' 'Sydney' 'Bristbane'
        params = (start_loc, other_loc)
        create_route = CreateRouteCommand(params=params, app_data=app_data)
        #Act
        create_route.execute()
        #Assert
        self.assertEqual(len(app_data._routes), 1)

    def test_CreateRoute_return_correctly_formated_string(self):
        #Arrange
        app_data = ApplicationData()
        start_loc = 'AliceSprings'
        other_loc = 'Adelaide' 'Melbourne' 'Sydney' 'Bristbane'
        params = (start_loc, other_loc)
        create_route = CreateRouteCommand(params=params, app_data=app_data)
        #Act
        result = create_route.execute()
        expected_output = f'Route with ID: 1 has been created!'
        #Assert
        self.assertEqual(expected_output, result)
    