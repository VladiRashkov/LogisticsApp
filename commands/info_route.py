from core.application_data import ApplicationData

class InfoRouteCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data

    def execute(self):
        route_id = int(self._params[0])
        route = self._app_data.find_route(route_id)
        if route is None:
            return f'Route with ID: {route_id} not found!'
        else:
            return route.view_route()


# Input: ViewRoute RouteId (1 param)
# Output:
# RouteID: 25
# Route status: open - > default message – changes when packages  assigned to route, and depends on the current date
# Route locations: Alice Spring (10/02 Saturday @ 06:00) → Adelaide (10/02 Saturday @ 20:00) → Sydney (11/02 Sunday @ 18:00) -> Melbourne (12/02 Monday @ 14:00) -> Brisbane (13/02 Tuesday @ 14:00)
# Route distance: 4041 km
# Route capacity: Capacity is still uncalculated. - > default message – changes when packages  assigned to route from hub
# Route start date: 10/02 Saturday @ 06:00
# Route final ETA: 13/02 Tuesday @ 14:00
# PackageID: Package is still unassigned. - > default message – changes when packages  assigned to route from hub
# TruckID: Truck is still unassigned. - > default message – changes validation passes route capacity < truck capacity; route distance < truck max range, truck availability between route start date and route final ETA
