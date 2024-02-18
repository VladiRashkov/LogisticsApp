from core.application_data import ApplicationData
from commands.base_command import BaseCommand

class AddPackageToRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
    
    def execute(self):
        route_id = int(self.params[0])
        package_id = int(self.params[1])

        route = self.app_data.find_route(route_id)
        if route is None:
            return f'Route with ID: {route.id} not found!'
        
        route.add_packages(package_id)
        return f'Pakcage with ID: {package_id} has been added to route with ID: {route_id}'

# Input: AddPackageToRoute RouteId PackageId (2 params)
# Output: Package with ID: 21 has been added to route with ID: 25!