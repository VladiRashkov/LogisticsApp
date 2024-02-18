import unittest
from commands.find_trucks import FindTrucks
from core.application_data import ApplicationData
from commands.create_trucks import CreateTrucks

class Find_Truck_Should(unittest.TestCase): 
    def test_find_trucks_working_properly(self): 
        #Arrange
        app_data = ApplicationData()
        create_trucks = CreateTrucks(params=None, app_data=app_data)
        find_trucks = FindTrucks(params=None, app_data=app_data)
        #Act 
        create_trucks.execute()
        find_trucks.execute()
        #Assert
        self.assertEqual(len(find_trucks.app_data.trucks), 40)

    def test_FIndTruck_truck_prints_buzy_when_truck_is_unavailable(self): #TODO waiting for other command assigntruck 
                                                              #to route or can be tested in assign truck to route test
        #Arrange
        app_data = ApplicationData()
        create_trucks = CreateTrucks(params=None, app_data=app_data)
        find_trucks = FindTrucks(params=None, app_data=app_data)

    def test_find_trucks_appends_to_AvailableTrucks(self):
        #Arrange
        app_data = ApplicationData()
        create_truck = CreateTrucks(params=None, app_data=app_data)
        find_trucks = FindTrucks(params=None, app_data=app_data)
        #Act
        create_truck.execute()
        find_trucks.execute()
        #Assert
        for truck in app_data._trucks:
            self.assertEqual(truck, )


    def test_find_truck_prints_correctly_formated_str(self):
        pass
