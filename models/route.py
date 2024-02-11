from datetime import datetime, timedelta
from locations import Locations 

class Route:
    id = 0

    @classmethod
    def next_id(cls):
        cls.id += 1
        return cls.id
    
    start_date_time = datetime.today()

    @classmethod
    def next_date(cls):
        replace_hour = cls.start_date_time.replace(hour=6)
        replace_minute = replace_hour.replace(minute=00)
        cls.start_date_time = replace_minute + timedelta(days=1)
        return cls.start_date_time
    
    def __init__(self, strat_location: Locations, other_locations: Locations) -> None:
        self.start_location = strat_location
        self.other_locations = other_locations
        self.route_id = Route.next_id()
        self.start_date_time = Route.next_date()

    def distance(self):
        distance = 0
        current_location = self.start_location
        for location in self.other_locations:
            key_locations_distance = f'{current_location}-{location}'
            distance += Locations.locations_distance[key_locations_distance]
            current_location = location
        return distance
    
    def final_eta(self):
        date_time = self.start_date_time
        current_location = self.start_location
        for location in self.other_locations:
            key_locations_time = f'{current_location}-{location}'
            locations_time = Locations.locations_time[key_locations_time]
            date_time += timedelta(hours=locations_time)
            current_location = location
            return date_time.strftime('%d/%m %A @ %H:%M')
        
    def to_string(self):
        date_time = self.start_date_time
        current_location = self.start_location 
        locations_list = []
        for location in self.other_locations:
            key_locations_time = f'{current_location}-{location}'
            locations_time = Locations.locations_time[key_locations_time]
            date_time += timedelta(hours=locations_time)
            locations_list.append(f'{location} {date_time.strftime('%d/%m %A @ %H:%M')}')
            current_location = location
        return (f'New route has been created:\n'
                f'RouteID: #{self.route_id}\n'
                f'Locations: {self.start_location} ({self.start_date_time.strftime('%d/%m %A @ %H:%M')}) → {" → ".join(locations_list)}\n'
                f'Total distance: {self.distance()} km\n'
                f'Start date: {self.start_date_time.strftime('%d/%m %A @ %H:%M')}\n'
                f'Final ETA: {self.final_eta()}')

route1 = Route('Alice Springs', ['Adelaide', 'Melbourne', 'Sydney', 'Bristbane'])
print(route1.to_string())
route2 = Route('Melbourne', ['Sydney', 'Bristbane'])
print(route2.to_string())


    # # old code:
    # def __init__(self, start_location: Locations, other_location: Locations) -> None:
    #     self.route_id = Route.next_id()
    #     self._id = id  # check how to not mess up 
    #     self._locations = []
    #     # self._start_date_time = datetime.today()

    #     # self._package = []  # to follow how to connect with model packages.py
    #     # self._truck = []  # to follow how to connect with model truck.py

    # @property
    # def id(self):
    #     return self._id
    
    # @property
    # def start_location(self):
    #     return self._start_location
    
    # @start_location.setter
    # def start_location(self, value):
    #     if value not in Locations.locations:
    #         raise ValueError('Please enter a supported location!')
        
    #     self._start_location = value
    
    # @property
    # def end_location(self):
    #     return self._end_location
    
    # @end_location.setter
    # def end_location(self, value):
    #     if value not in Locations.locations:
    #         raise ValueError('Please enter a supported location!')
        
    #     self._end_location = value
    
    # @property
    # def other_locations(self):
    #     return tuple(self._other_locations)
    
    
    # def add_other_location(self, location):
    #     if location not in Locations.locations:
    #         raise ValueError('Please enter a supported location!')
        
    #     self._other_locations.append(location)

    # def date_time(): # not sure about this
    #     start_date_time = datetime.today()
    #     change_hour = start_date_time.replace(hour=6)
    #     change_minutes = change_hour.replace(minute=00)
    #     start_date_time = change_minutes + timedelta(days=1)
        
    #     return start_date_time.strftime('%d/%m %A @ %H:%M')
    
    
    # def next_date_time():
    #     start_date_time = datetime.today()
    #     change_hour = start_date_time.replace(hour=6)
    #     change_minutes = change_hour.replace(minute=00)
    #     start_date_time = change_minutes + timedelta(days=1)
    #     start_date_time += timedelta(hours=10)

    #     return start_date_time.strftime('%d/%m %A @ %H:%M')


    # # string that shows a list of the scheduled routes
    # def info_route(self):
    #     pass

    # # in the application_data.py - appends a route to the schedule if the route hasn't been created already (attribute: self._routes = [])
    # def create_route():
    #     pass

    # # in the application_data.py - if the route we are looking for doeasn't exist it will show an error and that means we have to create one (attribute: self._routes = [])
    # def show_route(): 
    #     pass

    # # in the application_data.py - checks if the route we are looking for exists (attribute: self._routes = [])
    # def is_route_scheduled(): 
    #     pass 
    
    # # in the application_data.py - appends a package to an existing route (attribute: self._package_routes = [])
    # def add_package_to_route():
    #     pass

    # # in the application_data.py - removes a package from the existing route when end location has been reached (attribute: self._package_routes = [])
    # def remove_package_to_route():
    #     pass

    # # in the application_data.py - appends a truck to an existing route (attribute: self._truck_routes = [])
    # def add_truck_to_route():
    #     pass

    # # in the application_data.py - removes a truck from the existing route when end location has been reached (attribute: self._truck_routes = [])
    # def remove_truck_to_route():
    #     pass
        
    # commands to follow: create_route; show_route; update_route(add_package_to_route; add_truck_to_route; remove+package_from_route; remove_truck_from_route)