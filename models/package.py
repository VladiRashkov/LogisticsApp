from models.status import PackageStatus
from datetime import datetime



class Package:
    _id_counter = 1

    def __init__(self, start, end, weight: int, username):
        self._id = Package._id_counter
        Package._id_counter += 1
        self._start = start
        self._end = end
        self._weight = weight
        self._status = PackageStatus.UNASSIGNED
        self._date = datetime.now().strftime('%d/%m %A @ %H:%M')
        self._username = username

    def __str__(self):
        return f'Package {self._id}: from {self._start} to {self._end}, {self._weight} kg. Owner:{self._username}'
        
    
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value <= 0:
            raise ValueError('Invalid ID')
        self._id = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError('Weight must be a positive number')
        self._weight = value