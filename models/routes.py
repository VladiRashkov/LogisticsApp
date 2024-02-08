from datetime import datetime
from distance import Distance

class Routes:
    def __init__(self, id: int, start_loc: Distance, other_loc: Distance, departure: datetime, arrival: datetime) -> None:
        self._locations: list[Distance] = []
        self._id = id 
        self._start_loc = start_loc
        self._other_loc = other_loc
        self._departure = departure  # check how to use a date
        self._arrival = arrival

    @property
    def locations(self):
        return tuple(self._locations)
    
    @property
    def id(self):
        return self._id
    
    @property
    def start_loc(self):
        return self._start_loc
    
    @start_loc.setter
    def start_loc(self, value):
        if value not in Distance.locations:
            raise ValueError('The location is not in a supported area.')
        
        self._start_loc = value
    
    @property
    def other_loc(self):
        return self._other_loc
    
    @other_loc.setter
    def other_loc(self, value):
        if value not in Distance.locations:
            raise ValueError('The location is not in a supported area.')
        
        self._other_loc = value
    
    @property
    def departure(self):
        return self._departure
    
    @property
    def arrival(self):
        return self._arrival
    