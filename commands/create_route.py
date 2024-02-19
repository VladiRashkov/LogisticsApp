from core.application_data import ApplicationData
from models.route import Route

class CreateRouteCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data
      
    def execute(self):
        route_id = Route.id
        start_location = self._params[0]
        other_locations = self._params[1:]

        route = Route(start_location, *other_locations)
        self._app_data.add_route(route)

        return f'Route with ID: {route_id} has been created!'