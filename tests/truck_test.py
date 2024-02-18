import unittest
from models.truck import Truck
from models.status import TruckStatus

class Initializer_Should(unittest.TestCase):

    def test_create_id_adds_correctly(self):
        #Arrange
        test_truck1 = Truck()
        test_truck2 = Truck()
        test_truck3 = Truck()
        #Act & Assert
        result = test_truck3._truck_id
        self.assertEqual(result, 1003)

    def test_for_init_Truck_Scania_succesfully(self):
        #Arrange & Act
        test_truck = Truck()
        #Assert
        self.assertIsNotNone(test_truck)
        self.assertEqual(test_truck._status, TruckStatus.FREE)
        self.assertEqual(test_truck._brand, "Scania")
        self.assertEqual(test_truck._capacity, 42000)
        self.assertEqual(test_truck._range, 8000)
    
    def test_for_init_Truck_Man_succesfully(self):
        #Arrange & Act
        for test_truck in range(11):
            test_truck = Truck()

        #Assert
        self.assertIsNotNone(test_truck)
        self.assertEqual(test_truck._status, TruckStatus.FREE)
        self.assertEqual(test_truck._brand, "Man")
        self.assertEqual(test_truck._capacity, 37000)
        self.assertEqual(test_truck._range, 10000)

    def test_for_init_Truck_Actros_succesfully(self):
        #Arrange & Act
        for test_truck in range(30):
            test_truck = Truck()

        #Assert
        self.assertIsNotNone(test_truck)
        self.assertEqual(test_truck._status, TruckStatus.FREE)
        self.assertEqual(test_truck._brand, "Actros")
        self.assertEqual(test_truck._capacity, 26000)
        self.assertEqual(test_truck._range, 13000)
        

    def test_Truck_returns_correct_ids(self):
        #Arrange & Act
        for i in range(39):
            i = Truck()
        
        #Assert
        self.assertEqual(i._truck_id, 1039)

    def test_Truck_status_FREE(self):
        #Arrange & Act
        test_truck = Truck()
        #Assert
        self.assertEqual(test_truck._status, TruckStatus.FREE)

    def test_to_string(self):
        #Arrange & Act
        truck_test = Truck()
        expected_output = " Truck ID: 1001 --- Brand: Scania --- Status: Free,\n Capacity: 42000\n Range: 8000 \n ====================================================="
        #Assert
        self.assertEqual(expected_output, truck_test.to_string())