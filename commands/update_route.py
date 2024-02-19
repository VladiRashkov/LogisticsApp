from core.application_data import ApplicationData
from models.status import RouteStatus
from datetime import datetime

class UpdateRouteCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data
      

    def execute(self):
        route_id = int(self._params[0])

        route = self._app_data.find_route(route_id)

        today_date = datetime.today()

        if route is None:
            return f'Route with ID: {route_id} not found!'
        else:
            if route._packages != [] or route._truck != None:
                route._status = RouteStatus.next_route_status(RouteStatus.OPEN)
                return f'Route with ID: {route_id} has been updated with status: {route._status}!'
            elif today_date == route._start_date_time:
                route._status = RouteStatus.next_route_status(RouteStatus.SCHEDULED)
                return f'Route with ID: {route_id} has been updated with status: {route._status}!'
            elif today_date == route.eta():
                route._status = RouteStatus.next_route_status(RouteStatus.ON_ROUTE)
                return f'Route with ID: {route_id} has been updated with status: {route._status}!'
            elif route._packages == [] and route._truck == None:
                return f'Status for route with ID: {route_id} cannot be updated - truck and packages not assigned!'
            elif route._packages == [] or route._truck == None:
                route._status = RouteStatus.next_route_status(RouteStatus.ARRIVED)
                return f'Route with ID: {route_id} has been updated with status: {route._status}!'

# Input: UpdateRoute RouteId (1 param)
# Output: Route with ID: 25 has been updated with status: scheduled!