from core.application_data import ApplicationData
from commands.base_command import BaseCommand

class AddTruckToRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
       pass

# Input: AddTruckToRoute RouteId TruckId  (2 params)
# Output: Truck with ID: 1007 has been added to route with ID: 25!
