from models.package import Package
from models.route import Route
from models.truck import Truck
from models.user import User
from models.status import RouteStatus


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
    
    # Route
    @property
    def routes(self):
        return tuple(self._routes)
    
    def add_route(self, route: Route):
        self._routes.append(route)

    def find_route_id(self, route_id: int):
        for route in self._routes:
            if route._id == route_id:
               return route

        return None

    def cancel_route(self, route_id: int): 
        found_route = None
        for route in self._routes:
            if route._id == route_id:
               found_route = route

        if found_route is None:
            return False
        else:
            self._routes.remove(found_route)
            return True
    
    def find_package_id(self, package_id: int) -> Package:
        for package in self._packages:
            if package.id == package_id:
                return package

        return None
    
    def find_truck_id(self, truck_id: int) -> Truck:
        for truck in self._trucks:
            if truck._truck_id == truck_id:
                return truck

        return None

    def find_route_by_locations(self, start_location: Route, end_location: Route):
        for route in self._routes:
            n = start_location
            m = end_location
            locations = route.find_locations()
            for loc in range(len(locations)):
                if locations[loc] == n:
                    continue
                current = loc
                if locations[loc] == m and loc > current:
                    break
            return route
        return None
    
    def view_routes_status(self, status: RouteStatus):
        routes_status = []

        for route in self._routes:
            if route._status == status:
                routes_status.append(route)

        return routes_status