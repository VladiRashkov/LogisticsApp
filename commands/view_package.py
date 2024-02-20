from core.application_data import ApplicationData

class ViewPackageCommand:
    def __init__(self, params, app_data: ApplicationData):
        self._app_data = app_data
        self._params = params

    def execute(self):
        status_to_check = self._params[0].capitalize()
        unassigned = []
        assigned = []
        in_progress = []
        delivered = []
        
        for package in self._app_data.packages:
            if status_to_check == package.status:
                if status_to_check == "Unassigned":
                    unassigned.append(package)
                elif status_to_check == "Assigned":
                    assigned.append(package)
                elif status_to_check == "In_progress":
                    in_progress.append(package)
                elif status_to_check == "Delivered":
                    delivered.append(package)
                    
        if status_to_check == "Unassigned":
            return f"{'; '.join(map(str, unassigned))}"
        elif status_to_check == "Assigned":
            return f"{'; '.join(map(str, assigned))}"
        elif status_to_check == "In_progress":
           return f"{';'.join(map(str, in_progress))}"
        elif status_to_check == "Delivered":
            return f"{';'.join(map(str, delivered))}"
    #additionally takes the ETA from the route if it is assigned
    # route that is assigned to route ID

