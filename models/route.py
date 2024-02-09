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
    def departure(self, location: Schedule, date: datetime):
        pass
    
    # shows the other and the end locations of the scheduled route and the expected arrival time
    def arrival(self, location: Schedule, date: datetime):
        pass

    # add a location to a route which will be a scheduled one
    def add_locaton(self, location: Schedule): 
        pass

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






































# #experiments:
# now = datetime.now().strftime('%a, %d %B %Y')
# print(now)
# today = datetime.today().strftime('%a, %d %B %Y')
# print(today)
# departure = datetime.today() + timedelta(days =1)
# print(departure.strftime('%a, %d %B %Y'))
# arrival = departure + timedelta(days=2)
# print(arrival.strftime('%a, %d %B %Y'))
# time_now = datetime.now()
# time_now = time_now.strftime('%H:%M')
# print(time_now)
# time_future = datetime.today() + timedelta(hours=10)
# print(time_future.strftime('%H:%M'))
# date_hour = datetime.today()
# print(date_hour.strftime('%d/%m %A @ %H:%M'))
# date_hour = date_hour + timedelta(days=1, hours=2)
# print(date_hour.strftime('%d/%m %A @ %H:%M'))