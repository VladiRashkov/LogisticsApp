from models.package import Package
from models.route import Route
from models.truck import Truck
from models.user import User


class ApplicationData:
    def __init__(self):
        self._packages: list[Package] = []
        self._routes: list[Route] = []
        self._trucks: list [Truck] = []
        self._users = []
        
    #User
    @property
    def users(self):
        return tuple(self._users)
    
    def add_user(self, user:User):
        self.users.append(user)

    #Package   
    @property
    def packages(self):
        return tuple(self._packages)
    
    def add_package(self, package: Package):
        self._packages.append(package)
        
    #Truck
    @property
    def trucks(self):
        return tuple(self._trucks)


    def create_trucks(self, truck: Truck):
        self._trucks.append(truck)
    
    # Route:
    @property
    def routes(self):
        return tuple(self._routes)
    
    def add_route(self, route: Route):
        self._routes.append(route)

    def find_route(self, id: int):
        for route in self._routes:
            if route._id == id:
               return route

        return None

    def cancel_route(self, id: int): # for the route_update command???
        found_route = None
        for route in self._routes:
            if route._id == id:
               found_route = route

        if found_route is None:
            return False
        else:
            self._routes.remove(found_route)
            return True
    
    def find_package(self, id: int):
        for route in self._routes:
            for package in route._packages:
                if package.id == id:
                    return package

        return None
    
    def remove_package(self, id: int):
        found_package = None
        for route in self._routes:
            for package in route._packages:
                if package.id == id:
                    found_package = package

        if found_package is None:
            return False
        else:
            self._routes.remove(found_package)
            return True
        
    def find_truck(self, id: int):
        for route in self._routes:
            if route._truck == id:
                return id

        return None
    
    def remove_truck(self, id: int):
        found_truck = None
        for route in self._routes:
            if route._truck == id:
                found_truck = id

        if found_truck is None:
            return False
        else:
            self._routes.remove(found_truck)
            return True
