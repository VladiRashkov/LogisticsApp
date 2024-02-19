from core.application_data import ApplicationData
from commands.base_command import BaseCommand

class FindRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)
        
    def execute(self):
        start_location = self.params[0]
        end_location = self.params[1]

        route = self.app_data.find_route_by_locations(start_location, end_location)

        if route is None:
            return f'Route from {start_location} to {end_location} not found!'
        else:
            return f'Route locations: {route.locations()}'

# Input:  FindRoute AliceSprings Adelaide (2 params)
# Output: 
# Route locations: Alice Spring (10/02 Saturday @ 06:00) → Adelaide (10/02 Saturday @ 20:00) → Sydney (11/02 Sunday @ 18:00) -> Melbourne (12/02 Monday @ 14:00) -> Brisbane (13/02 Tuesday @ 14:00)
