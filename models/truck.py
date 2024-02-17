from models.constants.truck_status import TruckStatus
from models.constants.truck_type import TruckType


class Truck:
    Truck_ID = 1000
    
    def __init__(self): 
        # from core.application_data import ApplicationData
        # self._app_data = ApplicationData()
        self._truck_id = Truck.create_id() #!
        self._brand = ""
        self._status = TruckStatus.FREE
        self._capacity = 0
        self._range = 0
        for truck_type in TruckType.truck_types:
            if self._truck_id in truck_type["vehicle_ids"]:
                self._brand = truck_type["name"]
                self._capacity = truck_type["capacity"]
                self._range = truck_type["range"]
                # self._app_data._trucks.append(self)

    @classmethod
    def create_id(cls):
        cls.Truck_ID += 1
        return cls.Truck_ID
    
    
    def to_string(self):
        return f" Truck ID: {self._truck_id} --- Brand: {self._brand} --- Status: {self._status},\n Capacity: {self._capacity}\n Range: {self._range} \n ====================================================="
    