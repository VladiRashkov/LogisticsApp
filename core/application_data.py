from models.package import Package
from models.route import Route
from models.truck import Truck


class ApplicationData:
    def __init__(self):
        self._packages: list[Package] = []
        self._routes: list[Route] = []
        self._trucks: list [Truck] = []

    @property
    def packages(self):
        return tuple(self._packages)
    
    @property
    def trucks(self):
        return tuple(self._trucks)

    def add_package(self, package: Package):
        self._packages.append(package)

    def create_trucks(self, truck: Truck):
        self._trucks.append(truck)
    
    # for route needed - Elena
    @property
    def routes(self):
        return tuple(self._routes)

    def find_route(self, id: int):
        for route in self._routes:
            if route.id == id:
               return route

        return None

    def add_route(self, route: Route):
        self._routes.append(route)

    def remove_route(self, id: int):
        found_route = None
        for route in self._routes:
            if route.id == id:
               found_route = route

        if found_route is None:
            return False
        else:
            self._routes.remove(found_route)
            return True