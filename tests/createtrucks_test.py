import unittest
from commands.create_trucks import CreateTrucksCommand
from models.truck import Truck
from core.application_data import ApplicationData

class CreateTrucks_Should(unittest.TestCase):
    def test_execute_creates_trucks(self):
        # Arrange
        app_data = ApplicationData()
        create_trucks = CreateTrucksCommand(params=None, app_data=app_data)
        # Act
        create_trucks.execute()
        # Assert
        self.assertEqual(len(app_data._trucks), 40)
        
    def test_truck_is_isnstance(self):
        app_data = ApplicationData()
        for truck in app_data._trucks:
            self.assertIsInstance(truck, Truck)