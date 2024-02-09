from datetime import datetime, timedelta
from models.schedule import Schedule

class Routes:
    def __init__(self, id: int, date: datetime) -> None:
        self._id = id  # check how to not mess up - random library 
        self._date = date 
        self._locations = []
    
    @property
    def id(self):
        return self._id
    
    @property
    def locations(self):
        return tuple(self._locations)
    
    @property
    def date(self):
        return self._date
    
    # shows the start location of the scheduled route and the departure time
    def departure(self, departure_date: datetime):
        return f'{departure_date}' # modify date accornig to prepared schedule
    
    # shows the other and the end locations of the scheduled route and the expected arrival time
    def arrival(self, arrival_date: datetime):
        return f'{arrival_date}' # modify date accornig to prepared schedule
    
    # add a location to a route which will be a scheduled one
    def add_locaton(self, location: Schedule): 
        if location not in Schedule.locations:
            raise ValueError(f'Please enter a supported location.')
        
        self._locations.append(location)

    # removes a location to a route which will be a scheduled one if the max range has been exceeded
    def remove_location(self, location: Schedule): 
        pass

    # shows a list of the scheduled routes
    def info_route(self):
        pass

    # in the application_data.py - appends a route to the schedule if the route hasn't been created already (attribute: self._routes = [])
    def create_route():
        pass

    # in the application_data.py - if the route we are looking for doeasn't exist it will show an error and that means we have to create one (attribute: self._routes = [])
    def show_route(): 
        pass

    # in the application_data.py - checks if the route we are looking for exists (attribute: self._routes = [])
    def is_route_scheduled(): 
        pass 
    
    # in the application_data.py - appends a package to an existing route (attribute: self._package_routes = [])
    def add_package_to_route():
        pass

    # in the application_data.py - removes a package from the existing route when end location has been reached (attribute: self._package_routes = [])
    def remove_package_to_route():
        pass

    # in the application_data.py - appends a truck to an existing route (attribute: self._truck_routes = [])
    def add_truck_to_route():
        pass

    # in the application_data.py - removes a truck from the existing route when end location has been reached (attribute: self._truck_routes = [])
    def remove_truck_to_route():
        pass