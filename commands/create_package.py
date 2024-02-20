from core.application_data import ApplicationData
from models.package import Package
from commands.validation_helpers import try_parse_int

class CreatePackageCommand:
    def __init__(self, params, app_data: ApplicationData):
        self._params = params
        self.app_data = app_data


    def execute(self):
        package_id = Package._id_counter
        start = self._params[0]
        end = self._params[1]
        weight = try_parse_int(self._params[2])
        username = self._params[3]
        package = Package(start, end, weight, username)

        self.app_data.add_package(package)

        return f'Package {package_id} from {start} to {end} of the {username}, {weight} kg accepted in {start} Hub.'