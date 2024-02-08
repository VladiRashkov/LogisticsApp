from models.hubs.constants.base_hub import BaseHub
from models.hubs.constants.destinations_for_package import Destination

class AliceSprings(BaseHub):
    def __init__(self, city_name, storage_kg):
        super().__init__(city_name, storage_kg)
        self.destination_SYD = []
        self.destination_DAR = []
        self.destination_BRI = []
        self.destination_PER = []
        self.destination_MEL = []
        self.destination_ADL = []
        self.total_weight = 0

    def add_package_to_storage(self, destination, package):
        if destination not in Destination.__dict__.values():
            raise ValueError('This destination is not valid')

        if destination == Destination.SYD:
            self.destination_SYD.append(package)
        elif destination == Destination.DAR:
            self.destination_DAR.append(package)
        elif destination == Destination.BRI:
            self.destination_BRI.append(package)
        elif destination == Destination.PER:
            self.destination_PER.append(package)
        elif destination == Destination.MEL:
            self.destination_MEL.append(package)
        elif destination == Destination.ADL:
            self.destination_ADL.append(package)
        else:
            raise ValueError('Invalid destination')

        # Update the total_weight
        self.total_weight += package.weight

    def load_truck_remove_packages(self, truck_free_space, start_destination, end_destination):
        truck_storage = []
        # Check if the truck has free space
        if truck_free_space > 0:
            if start_destination == Destination.ASP and end_destination == Destination.SYD:
                for package in self.destination_SYD:
                    # Check if the package fits into the truck
                    if package.weight <= truck_free_space:
                        truck_storage.append(package)
                        self.destination_ASP.remove(package)

            elif start_destination == Destination.SYD and end_destination == Destination.DAR:
                for package in self.destination_DAR:
                    if package.weight <= truck_free_space:
                        truck_storage.append(package)
                        self.destination_DAR.remove(package)

            elif start_destination == Destination.SYD and end_destination == Destination.ADL:
                for package in self.destination_ADL:
                    if package.weight <= truck_free_space:
                        truck_storage.append(package)
                        self.destination_ADL.remove(package)

            elif start_destination == Destination.SYD and end_destination == Destination.MEL:
                for package in self.destination_MEL:
                    if package.weight <= truck_free_space:
                        truck_storage.append(package)
                        self.destination_MEL.remove(package)

            elif start_destination == Destination.SYD and end_destination == Destination.PER:
                for package in self.destination_PER:
                    if package.weight <= truck_free_space:
                        truck_storage.append(package)
                        self.destination_PER.remove(package)

            elif start_destination == Destination.SYD and end_destination == Destination.BRI:
                for package in self.destination_BRI:
                    if package.weight <= truck_free_space:
                        truck_storage.append(package)
                        self.destination_BRI.remove(package)

        return truck_storage
    
    def reload_stock_from_West_to_East(self, start_destination, end_destination, truck_free_space, truck_storage):
        packages_to_remove = []

        if start_destination == Destination.PER and end_destination == Destination.ADL:
            for package in truck_storage:
                if package.end_destination == Destination.ADL:
                    self.destination_ADL.append(package)
                    self.total_weight += package.weight
                    truck_storage.remove(package)
                    truck_free_space -= package.weight

                    packages_to_remove.append(package)

        for package in packages_to_remove:
            truck_storage.remove(package)

        return truck_storage

