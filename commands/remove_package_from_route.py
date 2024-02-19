from core.application_data import ApplicationData

class RemovePackageFromRouteCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data

    def execute(self):
        route_id = int(self._params[0])
        package_id = int(self._params[1])

        if self._app_data.remove_package(package_id):
            return f'Package with ID: {package_id} has been removed from route with ID: {route_id}!'
        else:
            return f'Package with ID: {package_id} not found!'


# Input: RemovePackageFromRoute RouteId PackageId (2 params)
# Output: Package with ID: 21 has been removed from route with ID: 25!