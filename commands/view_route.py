from core.application_data import ApplicationData
from models.status import RouteStatus

class ViewRouteCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data

    def execute(self):
        on_route = self._app_data.view_routes_status(RouteStatus.OPEN)

        on_route_list = []
        for route in on_route:
            package_weights = sum(package.weight for package in route._packages)
            info = (f'RouteID: {route._id}\n'
                   f'Route status: {route._status}\n'
                   f'Route locations: {route.locations()}\n'
                   f'Route total distnce: {route.distance()}\n'
                   f'Route capacity: {package_weights}\n'
                   f'Route start date: {route._start_date_time.strftime('%d/%m %A @ %H:%M')}\n'
                   f'Route final ETA: {route.eta()}\n'
                   f'Route current ETA: {route.current_eta()}')
            on_route_list.append(info)
            on_route_string = f'{''.join(on_route_list)}'
        return on_route_string