from core.application_data import ApplicationData

class ViewPackage():
    def __init__(self, params, app_data: ApplicationData):
        self._app_data = app_data
        self._params = params

    def execute(self):
        status_to_check = self._params[0].capitalize()

        
        if status_to_check == "Unassigned":
            unassigned = [str(package) for package in self._app_data.packages]
            return "\n".join(unassigned)
        elif status_to_check =="Assigned":
            assigned = [str(package) for package in self._app_data.packages]
            return "\n".join(assigned)
        elif status_to_check == "In progress":
            in_progress = [str(package) for package in self._app_data.packages]
            return "\n".join(in_progress)
        elif status_to_check == "Delivered":
            delivered = [str(package) for package in self._app_data.packages]
            return "\n".join(delivered)
    #additionally takes the ETA from the route if it is assigned
    # route that is assigned to route ID

