from core.application_data import ApplicationData
from commands.base_command import BaseCommand

class ViewRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        pass