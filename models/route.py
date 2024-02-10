from datetime import datetime, timedelta
from models.locations import Locations

class Routes:
    def __init__(self, id: int, start_location: str, end_location: str, start_date_time: datetime) -> None:
        self._date_generator(start_date_time)

        self._id = id  # check how to not mess up 
        self._start_location = start_location
        self._end_location = end_location
        self._other_locations = []
        self._start_date_time = start_date_time

        # self._package = []  # to follow how to connect with model packages.py
        # self._truck = []  # to follow how to connect with model truck.py

    @property
    def id(self):
        return self._id
    
    @property
    def start_location(self):
        return self._start_location
    
    @start_location.setter
    def start_location(self, value):
        if value not in Locations.locations:
            raise ValueError('Please enter a supported location!')
        
        self._start_location = value
    
    @property
    def end_location(self):
        return self._end_location
    
    @end_location.setter
    def end_location(self, value):
        if value not in Locations.locations:
            raise ValueError('Please enter a supported location!')
        
        self._end_location = value
    
    @property
    def other_locations(self):
        return tuple(self._other_locations)
    
    @property
    def start_date_time(self):
        return self._start_date_time.

    def date_generator(self, start_date_time):
        start_date_time = datetime.today()
        current = start_date_time .strftime('%d/%m %A @ %H:%M')
        modified_start_hour = start_date_time .replace(hour=6)
        current = modified_start_hour.strftime('%d/%m %A @ %H:%M')
        modified_start_minute = modified_start_hour.replace(minute=00)
        # current = modified_start_minute.strftime('%d/%m %A @ %H:%M')
        current = modified_start_minute
        return current.strftime('%d/%m %A @ %H:%M') 
    

    # # shows a list of the scheduled routes
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