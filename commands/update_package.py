from models.user import User
from core.application_data import ApplicationData
from commands.validation_helpers import try_parse_int
from models.status import Statuses
from datetime import datetime

class UpdatePackageCommand:
    def __init__(self, params, app_data: ApplicationData):
        self._app_data = app_data
        self._params = params
        

    def execute(self):
        format_string = "%d/%m %A @ %H:%M"
        input_package_id = try_parse_int(self._params[0])
        
        start_datetime_string = f"{self._params[1]} {self._params[2]} {self._params[3]} {self._params[4]}"
        input_start = datetime.strptime(start_datetime_string, format_string)
        input_start_formatted = input_start.strftime(format_string)
        eta_datetime_string = f"{self._params[5]} {self._params[6]} {self._params[7]} {self._params[8]}"
        input_eta = datetime.strptime(eta_datetime_string, format_string)
        input_eta_formatted = input_eta.strftime(format_string)
        
        
        
                
        for package in self._app_data.packages:
            if package.id == input_package_id:
                if package.date < input_start_formatted:
                    package.status = Statuses.ASSIGNED
                    return f"Package with ID:{package.id} is on status: {package.status}! ETA: {input_eta_formatted}"
                elif package.date >= input_start_formatted and package.date<input_eta_formatted:
                    package.status = Statuses.INPROGRESS
                    return f"Package with ID:{package.id} is on status: {package.status}! ETA: {input_eta_formatted}"
                elif package.date >=input_eta_formatted:
                    package.status = Statuses.DELIVERED
                    return f"Package with ID:{package.id} is on status: {package.status}! ETA: {input_eta_formatted}"
                
                
        for package in self._app_data.packages:
            if package.date < input_start_formatted:
                package.status=Statuses.ASSIGNED
            elif package.date >= input_start_formatted and package.date<input_eta_formatted:
                package.status = Statuses.INPROGRESS
            elif package.date >=input_eta_formatted:
                package.status = Statuses.DELIVERED
        # if input_status =="assigned".lower():
        #     for package in self._app_data.packages:
        #         if package.id == input_package_id:
        #             package.status=Statuses.ASSIGNED

        

                    