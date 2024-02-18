from core.application_data import ApplicationData
from commands.base_command import BaseCommand

class UpdateRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        pass

# Input: UpdateRoute RouteId (1 param)
# Output: Route with ID: 25 has been updated with status: scheduled!
    
# changes to follow?