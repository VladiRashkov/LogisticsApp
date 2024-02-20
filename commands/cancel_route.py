from core.application_data import ApplicationData

class CancelRouteCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data
      
    def execute(self):
        route_id = int(self._params[0])
        
        if self._app_data.cancel_route(route_id):
            return f'Route with ID: {route_id} has been cancelled'
        else:
            return f'Route with ID: {route_id} not found!'