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
    def routes(self):
        return tuple(self._routes)
    
    @property
    def trucks(self):
        return tuple(self._trucks)

    def add_package(self, package: Package):
        self._packages.append(package)

    def create_route(self, route: Route):
        self._routes.append(route)

    def show_trucks(self, truck: Truck):
        self._trucks.append(truck)
    
    