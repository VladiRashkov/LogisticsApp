from core.application_data import ApplicationData
from models.status import TruckStatus

class UpdateTruck:

    def __init__(self, params, app_data: ApplicationData) -> None:
        self.params = params
        self.app_data = app_data

    def execute(self):
        truck_id = int(self.params[0])
        truck_to_update = next((truck for truck in self.app_data._trucks if truck._truck_id == truck_id), None)

        if truck_to_update._status == TruckStatus.FREE:
            truck_to_update._status = TruckStatus.BUSY
            print(f'Truck {truck_id} updated to busy')
            
        elif truck_to_update._status == TruckStatus.BUSY:
            truck_to_update._status = TruckStatus.FREE 
            print(f'Truck {truck_id} updated to free')
            
        else:
            print(f'Truck with ID {truck_id} not found')
