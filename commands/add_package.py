from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from models.package import Package

class AddPackageCommand(BaseCommand):
    def __init__(self, params, app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        package_id = int(self.params[0])
        start = self.params[1]
        end = self.params[2]
        weight = int(self.params[3])
        contact_info = self.params[4]

        package = Package(package_id, start, end, weight, contact_info)
        self.app_data.add_package(package)

        return f"Package {package_id} from {start} to {end}, {weight} kg from {contact_info} accepted in {start} Hub."
