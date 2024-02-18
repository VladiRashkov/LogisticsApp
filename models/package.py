from models.status import PackageStatus
from datetime import datetime
from models.user import User
from models.route import Route


class Package:
    _id_counter = 1

    def __init__(self, start, end, weight: int, username):
        self.id = Package._id_counter
        Package._id_counter += 1
        self.start = start
        self.end = end
        self.weight = weight
        self.status = PackageStatus.UNASSIGNED
        self.date = datetime.now()
        self.username = username

    def __str__(self):
        return f"Package {self.id}: from {self.start} to {self.end}, {self.weight} kg. Owner:{self.username}"
        
    
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value <= 0:
            raise ValueError("Invalid ID")
        self._id = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be a positive number")
        self._weight = value