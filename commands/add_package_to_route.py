from core.application_data import ApplicationData

class AddPackageToRouteCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data
    
    def execute(self):
        route_id = int(self._params[0])
        package_id = int(self._params[1])

        route = self._app_data.find_route(route_id)
        if route is None:
            return f'Route with ID: {route.id} not found!'
        
        route.add_packages(package_id)
        return f'Pakcage with ID: {package_id} has been added to route with ID: {route_id}'

# Input: AddPackageToRoute RouteId PackageId (2 params)
# Output: Package with ID: 21 has been added to route with ID: 25!