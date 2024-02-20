# import unittest
# from commands.info_route import InfoRouteCommand
# from commands.create_route import CreateRouteCommand
# from core.application_data import ApplicationData

# class InfoRoute_Should(unittest.TestCase):
#     def test_InfoTruck_returns_route_not_found(self):
#         # Arrange
#         app_data = ApplicationData()
#         start_loc = 'AliceSprings'
#         other_loc = ['Adelaide', 'Melbourne', 'Sydney', 'Brisbane']
#         params = (start_loc, other_loc)
#         create_route = CreateRouteCommand(params=params, app_data=app_data)
#         info_route = InfoRouteCommand(params=[1], app_data=app_data)
#         expected_output = 

#         # Act
#         create_route.execute()
#         result = info_route.execute()

#         # Assert
#         self.assertEqual(expected_output, result)