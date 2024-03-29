from models.status import TruckStatus
from models.truck_type import TruckType


class Truck:
    Truck_ID = 1000
    
    def __init__(self): 
        self._truck_id = Truck.create_id() 
        self._brand = ""
        self._status = TruckStatus.FREE
        self._capacity = 0
        self._range = 0
        for truck_type in TruckType.truck_types:
            if self._truck_id in truck_type['vehicle_ids']:
                self._brand = truck_type['name']
                self._capacity = truck_type['capacity']
                self._range = truck_type['range']

    @classmethod
    def create_id(cls):
        cls.Truck_ID += 1
        return cls.Truck_ID
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, new_status):
        if new_status not in TruckStatus:
            raise ValueError('New status is invalid')
        else:
            self._status = new_status
    
    def to_string(self):
        return f' Truck ID: {self._truck_id} --- Brand: {self._brand} --- Status: {self._status},\n Capacity: {self._capacity}\n Range: {self._range} \n ====================================================='
    