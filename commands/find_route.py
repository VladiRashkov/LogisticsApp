from core.application_data import ApplicationData

class FindRouteCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data
        
    def execute(self):
        start_location = self._params[0]
        end_location = self._params[1]

        route = self._app_data.find_route_by_locations(start_location, end_location)

        if route is None:
            return f'Route from {start_location} to {end_location} not found!'
        else:
            return f'Route locations: {route.locations()}'

# Input:  FindRoute AliceSprings Adelaide (2 params)
# Output: 
# Route locations: Alice Spring (10/02 Saturday @ 06:00) → Adelaide (10/02 Saturday @ 20:00) → Sydney (11/02 Sunday @ 18:00) -> Melbourne (12/02 Monday @ 14:00) -> Brisbane (13/02 Tuesday @ 14:00)
