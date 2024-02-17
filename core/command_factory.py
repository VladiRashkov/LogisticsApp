from commands.create_package import CreatePackageCommand
from commands.add_truck_to_route import AddTruckToRoute
from core.application_data import ApplicationData
from commands.create_route import CreateRouteCommand
from commands.register_customer import RegisterCustomer
from commands.find_trucks import FindTrucks
from commands.create_trucks import CreateTrucks

class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "registercustomer":
            return RegisterCustomer(params, self._app_data)
        if cmd.lower() == "createpackage":
            return CreatePackageCommand(params, self._app_data)
        if cmd.lower() == "addtrucktoroute":
            return AddTruckToRoute(params, self._app_data)
        if cmd.lower() == "createroute":
            return CreateRouteCommand(params, self._app_data)
        if cmd.lower() == "createtrucks":
            return CreateTrucks(params, self._app_data)
        if cmd.lower() == "findtrucks":
            return FindTrucks(params, self._app_data)
        
        raise ValueError(f'Invalid command name: {cmd}!')
