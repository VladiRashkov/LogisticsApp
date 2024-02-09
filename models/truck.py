from models.vehicle import Vehicle
class Truck:

    def __init__(self, vehicle_id):
        vehicle_data = Vehicle.find_vehicle_by_id(vehicle_id)
        if vehicle_data:
            self.id = vehicle_id
            self.name = vehicle_data['name']
            self.capacity = vehicle_data['capacity']
            self.max_range = vehicle_data['max_range']
            self.decrement_number_of_vehicles(vehicle_id)

        else:
            raise ValueError(f"No vehicle found with id {vehicle_id}")


    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Capacity: {self.capacity} kg\n"
            f"Max Range: {self.max_range} km"
        )