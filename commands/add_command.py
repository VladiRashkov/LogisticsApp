from Commands.base_command import BaseCommand
from Core.application_data import ApplicationData

class AddPackageCommand(BaseCommand):
    def __init__(self, params, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        self._app_data.add_package()
