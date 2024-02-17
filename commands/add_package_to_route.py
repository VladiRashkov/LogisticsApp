from core.application_data import ApplicationData
from commands.base_command import BaseCommand

class AddPackageToRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
    
    def execute(self):
        pass

# Input: AddPackageToRoute RouteId PackageId weight (3 params)
# Output: Package with ID: 21 has been added to route with ID: 25!
