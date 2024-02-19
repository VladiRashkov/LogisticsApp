import unittest
from commands.update_truck import UpdateTruckCommand
from commands.create_trucks import CreateTrucksCommand
from core.application_data import ApplicationData
from models.status import TruckStatus

class UpdateTruckCommand_Should(unittest.TestCase):
    
    def test_changes_status_to_free(self):
        #Arrange
        app_data = ApplicationData()
        truck_id = '1001'
        create_trucks = CreateTrucksCommand(params=None, app_data=app_data)
        change_status = UpdateTruckCommand(params=[truck_id], app_data=app_data)
        expected_output = f'Truck {truck_id} updated to busy.'
        #Act
        create_trucks.execute()
        result = change_status.execute()
        #Assert
        self.assertEqual(result, expected_output)
        

    def test_changes_status_to_busy(self):
        #Arrange
        app_data = ApplicationData()
        truck_id = '1001'
        create_trucks = CreateTrucksCommand(params=None, app_data=app_data)
        change_status = UpdateTruckCommand(params=[truck_id], app_data=app_data)
        expected_output = f'Truck {truck_id} updated to free.'
        #Act
        create_trucks.execute()
        result = change_status.execute()
        result = change_status.execute()
        #Assert
        self.assertEqual(result, expected_output)

