from core.application_data import ApplicationData
from commands.base_command import BaseCommand

class RemovePackageFromRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        pass

# Input: RemovePackageFromRoute RouteId PackageId (2 params)
# Output: Package with ID: 21 has been removed from route with ID: 25!