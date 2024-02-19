from core.application_data import ApplicationData

class RemovePackageFromRouteCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data
    
    def execute(self):
        route_id = int(self._params[0])
        package_id = int(self._params[1])

        route = self._app_data.find_route_id(route_id)
        if route is None:
            return f'Route with ID: {route_id} not found!'
        
        package = self._app_data.find_package_id(package_id)
        if package is None:
            return f'Package with ID: {package_id} not found!'
        
        route.remove_packages(package)

        return f'Pakcage with ID: {package_id} has been removed from route with ID: {route_id}!'