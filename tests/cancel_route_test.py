import unittest
from core.application_data import ApplicationData
from commands.cancel_route import CancelRouteCommand
from commands.create_route import CreateRouteCommand

class CancelRoute_Should(unittest.TestCase):
    
    def test_CancelRoute_removes_route_successfully(self):
        #Arrange
        app_data = ApplicationData()
        start_loc = 'AliceSprings'
        other_loc = 'Adelaide' 'Melbourne' 'Sydney' 'Bristbane'
        params = (start_loc, other_loc)
        create_route = CreateRouteCommand(params=params, app_data=app_data)
        cancel_route = CancelRouteCommand(params=[1], app_data=app_data)
        #Act
        create_route.execute()
        cancel_route.execute()
        #Arrange
        self.assertEqual(len(app_data._routes), 0)

    def test_CancelRoute_returns_correctly_formated_string_when_ID_is_VALID(self):
        #Arrange
        app_data = ApplicationData()
        start_loc = 'AliceSprings'
        other_loc = 'Adelaide' 'Melbourne' 'Sydney' 'Bristbane'
        params = (start_loc, other_loc)
        create_route = CreateRouteCommand(params=params, app_data=app_data)
        cancel_route = CancelRouteCommand(params=[1], app_data=app_data)
        expected_output = 'Route with ID: 1 has been cancelled!'
        #Act
        create_route.execute()
        result = cancel_route.execute()
        #Arrange
        self.assertEqual(expected_output, result)

    def test_CancelRoute_return_correctly_formated_string_when_ID_is_INVALID(self):
        #Arrange
        app_data = ApplicationData()
        start_loc = 'AliceSprings'
        other_loc = 'Adelaide' 'Melbourne' 'Sydney' 'Bristbane'
        params = (start_loc, other_loc)
        create_route = CreateRouteCommand(params=params, app_data=app_data)
        cancel_route = CancelRouteCommand(params=[2], app_data=app_data)
        expected_output = 'Route with ID: 2 not found!'
        #Act
        create_route.execute()
        result = cancel_route.execute()
        #Arrange
        self.assertEqual(expected_output, result)
