from core.application_data import ApplicationData
from commands.base_command import BaseCommand
from models.route import Route

class CreateRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
      
    def execute(self):
        route_id = Route.id
        start_location = self.params[0]
        other_locations = self.params[1:]

        route = Route(start_location, *other_locations)
        self.app_data.add_route(route)

        return f'Route with ID: {route_id} has been created!'


# Input: CreateRoute AliceSprings Adelaide Sydney Melbourne Bristbane (n params)
# Output: Route with ID: 1 has been created!

