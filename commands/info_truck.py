from core.application_data import ApplicationData

class InfoTruckCommand:
    def __init__(self, params, app_data: ApplicationData):
        self.params = params
        self.app_data = app_data

    def execute(self):
        truck_id = int(self.params[0])
        truck_info = next((truck for truck in self.app_data._trucks if truck._truck_id == truck_id), None)
        if truck_info:
            info_message = f'\n Information for Truck {truck_info._truck_id}: \n Status: {truck_info._status} | Capacity: {truck_info._capacity} | Range: {truck_info._range}'
            print(info_message)
            return info_message
        else:
            print(f'Truck ID not found')
            return 'Truck ID not found'
