class Truck:
    def __init__(self, truck_id, type, capacity, max_range, weight, start, end):
        self.truck_id = truck_id
        self.type = type
        self.capacity = capacity
        self.max_range = max_range
        self.weight = weight
        self.start = start
        self.end=end
        self.assigned_routes =[]
        