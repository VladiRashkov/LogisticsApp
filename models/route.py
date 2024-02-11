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
        # self._trucks = [] # not sure yet if this will be here
        # self._packages = [] # not sure yet if this will be here

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
    
    # def add_truck(self):  # not sure if this will be here
    #     pass
    
    # def add_package(self):  # not sure if this will be here
    #     pass

    def to_string(self):  # there will be changes for this method!
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

# examples:
# route1 = Route('Alice Springs', ['Adelaide', 'Melbourne', 'Sydney', 'Bristbane'])
# print(route1.to_string())
# route2 = Route('Melbourne', ['Sydney', 'Bristbane'])
# print(route2.to_string())
