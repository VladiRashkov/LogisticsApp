from models.user import User
from models.route import Route
from models.constants.statuses import Statuses
class Package:
    _id_counter = 1

    def __init__(self, start, end, weight: int):
        self.id = Package._id_counter
        Package._id_counter += 1
        self.start = start
        self.end = end
        self.weight = weight
        self.status = Statuses.UNASSIGNED
        #self.user = user
        #self.route: None| Route = route
        #add status of the package


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


    def to_list(self):
                    return [self.id, self.start, self.end, self.weight]




