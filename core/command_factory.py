from commands.add_package import AddPackageCommand
from commands.add_truck_to_route import AddTruckToRoute
from core.application_data import ApplicationData

class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "addpackage":
            return AddPackageCommand(params, self._app_data)
        if cmd.lower() == "addtrucktoroute":
            return AddTruckToRoute(params, self._app_data)
        return None