class Vehicle():
    vehicles_data = [
        {"vehicle_ids": range(1001, 1011), "name": "Scania", "capacity": 42000, "max_range": 8000,
         "number_of_vehicles": 10},
        {"vehicle_ids": range(1011, 1026), "name": "Man", "capacity": 37000, "max_range": 10000,
         "number_of_vehicles": 15},
        {"vehicle_ids": range(1026, 1041), "name": "Actros", "capacity": 26000, "max_range": 13000,
         "number_of_vehicles": 15}
    ]

    @classmethod
    def find_vehicle_by_id(cls, vehicle_id):
        for vehicle_data in cls.vehicles_data:
            if vehicle_id in vehicle_data['vehicle_ids']:
                return vehicle_data

    @classmethod
    def decrement_number_of_vehicles(cls, vehicle_id):
        vehicle_data = cls.find_vehicle_by_id(vehicle_id)
        if vehicle_data:
            vehicle_data['number_of_vehicles'] -= 1
        else:
            raise ValueError(f"No vehicle found with id {vehicle_id}")

