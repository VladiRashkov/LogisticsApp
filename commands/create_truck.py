from core.application_data import ApplicationData
import random
from models.constants.truck_status import TruckStatus
from models.truck import Truck

class Create_Truck:
    
    def __init__(self, params, app_data = ApplicationData):
        self._app_data = app_data
        self._params = params

    def execute(self):
        
        for _ in range(40):
            truck_type = random.choice(Truck.truck_types) #! check it because we have brand as well and probably it is doubled !
            truck_id = Truck.create_id()
            brand = truck_type["name"] #!!! Check 
            status = TruckStatus.FREE
            routes = []
            capacity = truck_type["capacity"]
            range = truck_type["range"]

            new_truck = Truck(truck_id, brand, status, routes, capacity, range)
            self._app_data.append(new_truck)
            print(f'Truck created {truck_type}, {truck_id}, {brand}, {status}, {routes}, {capacity}kg, {range}km')