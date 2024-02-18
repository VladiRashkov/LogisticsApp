from commands.create_package import CreatePackageCommand
from commands.register_customer import RegisterCustomer
from commands.find_trucks import FindTrucks
from commands.create_trucks import CreateTrucks
# for route:
from commands.add_package_to_route import AddPackageToRouteCommand
from commands.add_truck_to_route import AddTruckToRouteCommand
from commands.create_route import CreateRouteCommand
from commands.remove_package_from_route import RemovePackageFromRouteCommand
from commands.remove_truck_from_route import RemoveTruckFromRouteCommand
from commands.find_route import SearchRouteCommand
from commands.update_route import UpdateRouteCommand
from commands.Info_route import ViewRouteCommand

from core.application_data import ApplicationData

class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "registercustomer":
            return RegisterCustomer(params, self._app_data)
        if cmd.lower() == "createpackage":
            return CreatePackageCommand(params, self._app_data)
        if cmd.lower() == "createtrucks":
            return CreateTrucks(params, self._app_data)
        if cmd.lower() == "findtrucks":
            return FindTrucks(params, self._app_data)
        # for route:
        if cmd.lower() == 'addpackagetoroute':
            return AddPackageToRouteCommand(params, self._app_data)
        if cmd.lower() == 'addtrucktoroute':
            return AddTruckToRouteCommand(params, self._app_data)
        if cmd.lower() == 'createroute':
            return CreateRouteCommand(params, self._app_data)
        if cmd.lower() == 'removepackagefromroute':
            return RemovePackageFromRouteCommand(params, self._app_data)
        if cmd.lower() == 'removetruckfromroute':
            return RemoveTruckFromRouteCommand(params, self._app_data)
        if cmd.lower() == 'searchroute':
            return SearchRouteCommand(params, self._app_data)
        if cmd.lower() == 'updateroute':
            return UpdateRouteCommand(params, self._app_data)
        if cmd.lower() == 'viewroute':
            return ViewRouteCommand(params, self._app_data)
        
        raise ValueError(f'Invalid command name: {cmd}!')
