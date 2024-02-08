
class Package():

    def __init__(self, id: int, start, end, weight:int, contact_info:str):
        self.id = id
        self.start = start
        self.end = end
        self.weight = weight
        self.contact_info = contact_info


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

    def to_dict(self):
            return {
                "ID": self.id,
                "Start": str(self.start),
                "End": str(self.end),
                "Weight": self.weight,
                "Contact Info": self.contact_info
                }