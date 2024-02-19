from core.application_data import ApplicationData

class AddTruckToRouteCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data

    def execute(self):
        route_id = int(self._params[0])
        truck_id = int(self._params[1])

        route = self._app_data.find_route(route_id)
        if route is None:
            return f'Route with ID: {route.id} not found!'
        
        route.add_truck(truck_id)
        return f'Truck with ID: {truck_id} has been added to route with ID: {route_id}'


# Input: AddTruckToRoute RouteId TruckId  (2 params)
# Output: Truck with ID: 1007 has been added to route with ID: 25!
