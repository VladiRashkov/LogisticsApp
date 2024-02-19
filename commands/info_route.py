from core.application_data import ApplicationData

class InfoRouteCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data

    def execute(self):
        route_id = int(self._params[0])
        route = self._app_data.find_route_id(route_id)
        if route is None:
            return f'Route with ID: {route_id} not found!'
        else:
            return route.view_route()