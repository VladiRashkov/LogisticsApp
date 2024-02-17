from models.constants.statuses import Statuses
from datetime import datetime
from models.user import User
class Package:
    _id_counter = 1

    def __init__(self, start, end, weight: int, user: User):
        self.id = Package._id_counter
        Package._id_counter += 1
        self.start = start
        self.end = end
        self.weight = weight
        self.status = Statuses.UNASSIGNED
        self.date = datetime.now().strftime('%d/%m %A @ %H:%M')
        self.user = user
        

    def __str__(self):
        return f"Package {self.id}: from {self.start} to {self.end}, {self.weight} kg. Owner:{User}"


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