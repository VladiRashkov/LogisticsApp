from models.user import User
from core.application_data import ApplicationData
from commands.validation_helpers import try_parse_int
from models.status import PackageStatus
class UpdatePackage():
    def __init__(self, params, app_data: ApplicationData):
        self._app_data = app_data
        self._params = params

    def execute(self):
        input_package_id = try_parse_int(self._params[0])
        input_route_id = try_parse_int(self._params[1])
        input_status = self._params[2]
        input_eta = self._params[3]

        if input_status =="assigned".lower():
            for package in self._app_data.packages:
                if package.id == input_package_id:
                    package.status=PackageStatus.ASSIGNED

                    return f"Package with ID:{package.id} has been updated with status: {package.status}!"