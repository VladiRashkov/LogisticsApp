from core.application_data import ApplicationData
from commands.validation_helpers import try_parse_int

class InfoPackageCommand:
    def __init__(self, params, app_data: ApplicationData):
        self._params = params
        self.app_data = app_data

    def execute(self):
        id_input = try_parse_int(self._params[0])
        for package in self.app_data.packages:
            if package.id == id_input:
                return f"PackageID: {package.id}\nPackage weight: {package.weight} kg\nPackage start location: {package.start}\nPackage end location: {package.end}\nPackage entry date: {package._date}\nPackage final ETA:\nPackage status: {package.status}"







