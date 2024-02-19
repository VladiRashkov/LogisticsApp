import unittest
from commands.info_truck import InfoTruckCommand
from core.application_data import ApplicationData
from commands.create_trucks import CreateTrucksCommand

class InfoTruck_Should(unittest.TestCase):

    def test_execute_prints_correctly_formated_string(self):
        #Arrange
        app_data = ApplicationData()
        p = '1009'
        created_trucks = CreateTrucksCommand(params=None, app_data=app_data)
        info_trucks = InfoTruckCommand(params=[p], app_data=app_data)
        expected_output = f'\n Information for Truck {p}: \n Status: Free | Capacity: 42000 | Range: 8000'
        #Act
        trucks = created_trucks.execute()
        result = info_trucks.execute()
        
        #Assert
        self.assertEqual(result, expected_output)
        

        

    def test_execute_prints_str_when_id_is_not_found(self):
        #Arrange
        app_data = ApplicationData()
        p = '10000'
        created_trucks = CreateTrucksCommand(params=None, app_data=app_data)
        info_trucks = InfoTruckCommand(params=p, app_data=app_data)
        expected_output = f'Truck ID not found'
        #Act
        trucks = created_trucks.execute()
        result = info_trucks.execute()
        
        #Assert
        self.assertEqual(result, expected_output)
