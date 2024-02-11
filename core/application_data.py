from models.package import Package
from models.route import Route

class ApplicationData:
    def __init__(self):
        self._packages: list[Package] = []
        self._routes: list[Route] = []

    @property
    def packages(self):
        return tuple(self._packages)

    @property
    def routes(self):
        return tuple(self._routes)

    def add_package(self, package: Package):
        self._packages.append(package)

    def create_route(self, route: Route):
        self._routes.append(route)