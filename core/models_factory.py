# needed for route - Elena
from models.route import Route
from models.location import Location


class ModelsFactory:
    def __init__(self):
        self._route_id = 1

    def create_route(self, strat_location: Location, *other_locations: Location):
        new_route_id = self._route_id
        self._route_id += 1

        return Route(new_route_id, strat_location, *other_locations)
