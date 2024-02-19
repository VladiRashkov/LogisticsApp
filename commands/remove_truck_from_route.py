from core.application_data import ApplicationData

class RemoveTruckFromRouteCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data
        
    def execute(self):
        route_id = int(self._params[0])
        truck_id = int(self._params[1])

        if self._app_data.remove_truck(truck_id):
            return f'Truck with ID: {truck_id} has been removed from route with ID: {route_id}!'
        else:
            return f'Truck with ID: {truck_id} not found!'

# Input: RemoveTruckFromRoute RouteId TruckId  (2 params)
# Output: Truck with ID: 1007 has been removed from route with ID: 25!