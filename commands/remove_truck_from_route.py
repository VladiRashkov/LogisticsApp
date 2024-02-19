from core.application_data import ApplicationData

class RemoveTruckFromRouteCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data
        
    def execute(self):
        route_id = int(self._params[0])
        truck_id = int(self._params[1])

        route = self._app_data.find_route_id(route_id)
        if route is None:
            return f'Route with ID: {route_id} not found!'
        
        truck = self._app_data.find_truck_id(truck_id)
        if truck is None:
            return f'Truck with ID: {truck_id} not found!'
        
        route.remove_truck(truck)

        return f'Truck with ID: {truck_id} has been removed from route with ID: {route_id}!'