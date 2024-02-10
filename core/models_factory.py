from models.route import Routes

class ModelsFactory:
        def __init__(self) -> None:
                self._route_id = 1

        def create_route(self, start_location: str, end_location: str):
                route_id = self._route_id
                self._route_id += 1

                return Routes(route_id, start_location, end_location)
                      