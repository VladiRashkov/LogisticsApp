from core.application_data import ApplicationData
from models.constants.truck_status import TruckStatus
from models.truck import Truck
from models.constants.truck_type import TruckType


class ShowTrucks:
    
    def __init__(self, params, app_data=ApplicationData):
        self._app_data = app_data
        self._params = params

    def execute(self):
        self._app_data = ApplicationData()
        for truck in range(1001, 1041):
            new_truck = Truck()
            # new_truck._truck_id = truck_id
            self._app_data._trucks.append(new_truck)
        for truck in self._app_data._trucks:
            print(truck.to_string())

#Problem with last truck: outputs - None... Maybe range?   