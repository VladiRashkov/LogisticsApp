from datetime import datetime
from models.constants.truck_status import TruckStatus

import random


class Truck:
    Truck_ID = 1000

    truck_types = [
        {"vehicle_ids": range(1001, 1011), "name": "Scania", "capacity": 42000, "range": 8000},
        {"vehicle_ids": range(1011, 1026), "name": "Man", "capacity": 37000, "range": 10000},
        {"vehicle_ids": range(1026, 1041), "name": "Actros", "capacity": 26000, "range": 13000}
    ]

#truck_id , brand, status, routes = empty list, capacity, range
    def __init__(self, truck_id, brand, status, routes, capacity, range):
        self._truck_id = truck_id
        self._brand = self.validate_brand(self._truck_id)
        self._status = TruckStatus.FREE
        self._routes: list = [] # ASP - BRI - SYD
        self._capacity = self.validate_capacity()
        self._range = self.validate_range()

    @property
    def status(self):
        return self._status
    
    # @property
    # def current_location(self):
    #     if len(self._routes) == 0:
    #         self.status == TruckStatus.FREE
    #         return 'Not on any route'
    #     #Other cases
    #     return 'Driving'
        
    @classmethod
    def create_id(cls):
        cls.Truck_ID += 1
        return cls.Truck_ID
    
    def validate_brand(self, truck_id):
        if 1000 < truck_id <= 1011:
            return 'Scania'
            
        elif 1011 < truck_id <= 1026:
            return 'Man'
        
        elif 1026 < truck_id <= 1041:
            return 'Actros'
    
    def validate_capacity(self):
        if self._brand == 'Scania':
            return 42000
        elif self._brand == 'Man':
            return 37000
        elif self._brand == 'Actros':
            return 26000
        else:
            return 0
        
    def validate_range(self):
        if self._brand == 'Scania':
            return 8000
        elif self._brand == 'Man':
            return 10000
        elif self._brand == 'Actros':
            return 13000
        else:
            return 0
    
    def to_string(self):
        return f"Truck ID: {self._truck_id},\n Brand: {self._brand},\n Status: {self._status},\n Routes: {self._routes},\n Capacity: {self._capacity},\n Range: {self._range}"
    

# truck1 = Truck(truck_id=1001, brand="Scania", status=TruckStatus.FREE, routes=[], capacity=42000, range=8000)

# # Creating an instance using create_trucks method
# trucks_batch = Truck.create_trucks(3)

# # Printing details of each truck
# for truck in trucks_batch:
#     print(truck.to_string())