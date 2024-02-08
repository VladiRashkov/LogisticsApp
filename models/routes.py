from datetime import datetime, timedelta
from distance import Distance

class Routes:
    def __init__(self, id: int, start_loc: Distance, other_loc: Distance, departure: datetime, arrival: datetime) -> None:
        self._locations: list[Distance] = []
        self._id = id 
        self._start_loc = start_loc
        self._other_loc = other_loc
        self._departure = departure  
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
    


#experiments:
now = datetime.now().strftime('%a, %d %B %Y')
print(now)
today = datetime.today().strftime('%a, %d %B %Y')
print(today)
departure = datetime.today() + timedelta(days =1)
print(departure.strftime('%a, %d %B %Y'))
arrival = departure + timedelta(days=2)
print(arrival.strftime('%a, %d %B %Y'))
time_now = datetime.now()
time_now = time_now.strftime('%H:%M')
print(time_now)
time_future = datetime.today() + timedelta(hours=10)
print(time_future.strftime('%H:%M'))