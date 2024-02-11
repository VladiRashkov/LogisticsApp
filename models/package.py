from models.user import User
from models.route import Route
class Package():
    _id_counter = 1


    def __init__(self, start, end, weight: int, user:User):
        Package._id_counter +=1
        self.id = Package._id_counter
        self.start = start
        self.end = end
        self.weight = weight
        self.user = user
        #self.route: None| Route = route


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

    def __str__(self):
                    return (f"ID: {self.id}, "
                            f"Start: {str(self.start)}, "
                            f"End: {str(self.end)}, "
                            f"Weight: {self.weight}, "
                            f"Contact Info: {self.user}")