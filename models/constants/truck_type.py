class TruckType:
    truck_types = [
        {"vehicle_ids": range(1001, 1011), "name": "Scania", "capacity": 42000, "range": 8000},
        {"vehicle_ids": range(1011, 1026), "name": "Man", "capacity": 37000, "range": 10000},
        {"vehicle_ids": range(1026, 1041), "name": "Actros", "capacity": 26000, "range": 13000}
    ]

    @classmethod
    def find_vehicle_by_id(cls, truck_id):
        for truck_type in cls.truck_types:
            if truck_id in truck_type['vehicle_ids']:
                return truck_id
        return None #None if id is not found
    
    @classmethod
    def truck_capacity(cls, brand):
         
        if brand == 'Scania':
            return 42000
        elif brand == 'Man':
            return 37000
        elif brand == 'Actros':
            return 26000
        else:
            return 0