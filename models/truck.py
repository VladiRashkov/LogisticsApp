from datetime import datetime
from models.constants.truck_status import TruckStatus
from models.constants.truck_type import TruckType

class Truck:
    Truck_ID = 1000
#truck_id , brand, status, routes = empty list, capacity, range
    def __init__(self):
        self._truck_id = self.create_id()
        self._brand = self.validate_brand(self._truck_id)
        self._status = TruckStatus.FREE
        self._routes: list = [] # ASP - BRI - SYD
        self._capacity = self.validate_capacity()
        self._range = self.validate_range()

    @property
    def status(self):
        return self._status
    
    @property
    def current_location(self):
        if len(self._routes) == 0:
            self.status == TruckStatus.FREE
            return 'Not on any route'
        #Other cases
        return 'Driving'

            
    def free_truck_interval(self):
        intervals = []
        course =  len(self._routes)
        if course == 0:
            return #datetime anytime our truck is free
        if course == 1:
            #must be (datetime min from self.routes [0].start_time, calculation for estimate time(), datetime max)

        ###for course in self###
            pass

    def create_id(self):
        Truck.Truck_ID += 1
        return Truck.Truck_ID
    
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