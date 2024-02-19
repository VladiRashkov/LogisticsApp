from datetime import datetime, timedelta
from models.location import Location
from models.status import RouteStatus
from models.package import Package
from models.truck import Truck

class Route:
    id = 1

    start_date_time = datetime.today()

    def __init__(self, strat_location: Location, *other_locations: Location) -> None:
        self._start_location = strat_location
        self._other_locations = other_locations

        self._id = Route.id
        Route.id += 1
        self._start_date_time = Route.start_date_time.replace(hour=6, minute=00) + timedelta(days=1)
        self._status = RouteStatus.OPEN

        self._packages: list[Package] = []
        self._truck: Truck = None  


    @property
    def start_location(self):
        return self._start_location
    
    @property
    def other_locations(self):
        return self._other_locations
    
    @property
    def packages(self):
        return tuple(self._packages)

    def locations(self):
        date_time = self._start_date_time
        current_location = self._start_location 
        locations_list = []
        for location in self._other_locations:
            key_locations_time = f'{current_location}-{location}'
            locations_time = Location.locations_time[key_locations_time]
            date_time += timedelta(hours=locations_time)
            locations_list.append(f'{location} {date_time.strftime('%d/%m %A @ %H:%M')}')
            current_location = location
            locations = f'{self._start_location} ({self._start_date_time.strftime('%d/%m %A @ %H:%M')}) → {" → ".join(locations_list)}'
        return locations
    
    def find_locations(self): 
        find_locations_list = []
        find_locations_list.append(self.start_location)
        for location in self._other_locations:
            find_locations_list.append(location)
        return find_locations_list


    
    def distance(self):
        distance = 0
        current_location = self._start_location
        for location in self._other_locations:
            key_locations_distance = f'{current_location}-{location}'
            distance += Location.locations_distance[key_locations_distance]
            current_location = location
        return distance
    
    def eta(self):
        date_time = self._start_date_time
        current_location = self._start_location
        for location in self._other_locations:
            key_locations_time = f'{current_location}-{location}'
            locations_time = Location.locations_time[key_locations_time]
            date_time += timedelta(hours=locations_time)
            current_location = location
        return date_time.strftime('%d/%m %A @ %H:%M')
    
    def current_eta(self):
        current_date_time = datetime.today()
        current_location = self._start_location
        current_location_date_time = self._start_date_time
        for location in self._other_locations:
            key_locations_time = f'{current_location}-{location}'
            locations_time = Location.locations_time[key_locations_time]
            current_location_date_time += timedelta(hours=locations_time)

        if current_date_time > current_location_date_time:
            return current_location_date_time.strftime('%d/%m %A @ %H:%M')
        else:
            return f'Truck hasn\'t left yet!'
    
    def change_status(self):
        self._status = RouteStatus.next_route_status(self.status)

    def add_packages(self, package: Package): 
        self._packages.append(package)
    
    def add_truck(self, truck: Truck):
        range = Route.distance()
        capacity = sum(package.weight for package in self._packages)
        if range < truck._range and capacity < truck._capacity:
            self._truck = truck._truck_id
        else:
            raise ValueError(f'Please, enter another TruckID as this one is unsuitable.')
        
    def view_route(self):
        package_ids = [f'{package.id}' for package in self._packages]
        package_weights = sum(package.weight for package in self._packages)
        if len(package_ids) == 0 and self._truck == None:
            return (f'RouteID: {self._id}\n'
                    f'Route status: {self._status}\n'
                    f'Route locations: {self.locations()}\n'
                    f'Route total distnce: {self.distance()} km\n'
                    f'Route capacity: No packages assigned.\n'
                    f'Route start date: {self._start_date_time.strftime('%d/%m %A @ %H:%M')}\n'
                    f'Route final ETA: {self.eta()}\n'
                    f'PackageID: No packages assigned.\n'  
                    f'TruckID: No truck assigned.')
        else:
            return (f'RouteID: {self._id}\n'
                    f'Route status: {RouteStatus.next_route_status(RouteStatus.OPEN)}\n'
                    f'Route locations: {self.locations()}\n'
                    f'Route total distnce: {self.distance()} km\n'
                    f'Route capacity: {package_weights} kg\n'
                    f'Route start date: {self._start_date_time.strftime('%d/%m %A @ %H:%M')}\n'
                    f'Route final ETA: {self.eta()}\n'
                    f'PackageID: {package_ids}\n'  
                    f'TruckID: {self._truck}') 