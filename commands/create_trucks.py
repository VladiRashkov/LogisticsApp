from core.application_data import ApplicationData
from models.status import TruckStatus
from models.truck import Truck

class CreateTrucksCommand:
    
    def __init__(self, params, app_data: ApplicationData):
        self._app_data = app_data
        self._params = params

    def execute(self):
        for truck in range(1001, 1041):
            new_truck = Truck() 
            self._app_data._trucks.append(new_truck)

        trucks_string = []
        for truck in self._app_data._trucks:
            truck_str = truck.to_string()
            trucks_string.append(truck_str)
        trucks_string = '\n'.join(trucks_string)
        return trucks_string