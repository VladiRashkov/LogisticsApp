from datetime import datetime, timedelta
from models.location import Location
from models.status import Status
from models.package import Package
from models.truck import Truck

class Route:
    
    start_date_time = datetime.today()

    @classmethod
    def next_date_time(cls):
        replace_hour = cls.start_date_time.replace(hour=6)
        replace_minute = replace_hour.replace(minute=00)
        cls.start_date_time = replace_minute + timedelta(days=1)
        return cls.start_date_time
    
    def __init__(self, id: int, strat_location: Location, *other_locations: Location) -> None:
        self._id = id
        self._start_location = strat_location
        self._other_locations = other_locations
        self._start_date_time = Route.next_date_time()
        self._status = Status.OPEN
        self._package_ids: list[Package] = [] # to follow
        self._truck_id = None  # to follow

    @property
    def id(self):
        return self._id
    
    @property
    def start_location(self):
        return self._start_location
    
    @property
    def other_locations(self):
        return self._other_locations
    
    @property
    def package_ids(self):
        return tuple(self._package_ids)

    def locations(self):
        date_time = self.start_date_time
        current_location = self.start_location 
        locations_list = []
        for location in self.other_locations:
            key_locations_time = f'{current_location}-{location}'
            locations_time = Location.locations_time[key_locations_time]
            date_time += timedelta(hours=locations_time)
            locations_list.append(f'{location} {date_time.strftime('%d/%m %A @ %H:%M')}')
            current_location = location
            locations = f'{self.start_location} ({self.start_date_time.strftime('%d/%m %A @ %H:%M')}) → {" → ".join(locations_list)}'
        return locations
    
    def distance(self):
        distance = 0
        current_location = self.start_location
        for location in self.other_locations:
            key_locations_distance = f'{current_location}-{location}'
            distance += Location.locations_distance[key_locations_distance]
            current_location = location
        return distance
    
    def eta(self):
        date_time = self.start_date_time
        current_location = self.start_location
        for location in self.other_locations:
            key_locations_time = f'{current_location}-{location}'
            locations_time = Location.locations_time[key_locations_time]
            date_time += timedelta(hours=locations_time)
            current_location = location
            return date_time.strftime('%d/%m %A @ %H:%M')

    def add_packages(self): # def add_packages(self, package: Package):
        # self.packages.append(package)
        return f'Package is still unassigned.'

    def capacity(self):
        return f'Capacity is still uncalculated.'
    
    def change_status(self):
        self.status = Status.next_route_status(self.status)
    
    def add_truck(self):
            return f'Truck is still unassigned.'
    
    def view_route(self):  
        return (f'RouteID: {self._id}\n'
                f'Route status: {self._status}\n'
                f'Route locations: {self.locations()}\n'
                f'Route total distnce: {self.distance()} km\n'
                f'Route capacity: {self.capacity()}\n'
                f'Route start date: {self._start_date_time.strftime('%d/%m %A @ %H:%M')}\n'
                f'Route final ETA: {self.eta()}\n'
                f'PackageID: {self.add_packages()}\n'  # f'PackageID: {','.join({package_id} for package in self.package_ids)}\n'
                f'TruckID: {self.add_truck()}')  # f'TruckID: {self.truck_id}\n'