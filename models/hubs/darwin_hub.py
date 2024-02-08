from models.hubs.constants.base_hub import BaseHub
from models.hubs.constants.destinations_for_package import Destination

class Darwin(BaseHub):
    def __init__(self, total_weight):
        super().__init__(total_weight)
        self.destination_ASP = []
        self.destination_PER = []
        self.destination_BRI = []
        self.destination_SYD = []
        self.destination_MEL = []
        self.destination_ADL = []
        self.total_weight = 0
        self.packages_to_remove = []
        self.truck_storage = []

    def add_package_to_storage(self, destination, package):
        if destination not in Destination.__dict__.values():
            raise ValueError('This destination is not valid')

        if destination == Destination.ASP:
            self.destination_ASP.append(package)
        elif destination == Destination.DAR:
            self.destination_PER.append(package)
        elif destination == Destination.BRI:
            self.destination_BRI.append(package)
        elif destination == Destination.SYD:
            self.destination_SYD.append(package)
        elif destination == Destination.MEL:
            self.destination_MEL.append(package)
        elif destination == Destination.ADL:
            self.destination_ADL.append(package)
        else:
            raise ValueError('Invalid destination')

        # Update the total_weight
        self.total_weight += package.weight

    def load_truck_remove_packages(self, truck_free_space, start_destination, end_destination):
        
        # Check if the truck has free space
        if truck_free_space > 0:
            if start_destination == Destination.DAR and end_destination == Destination.ASP:
                for package in self.destination_ASP:
                    # Check if the package fits into the truck
                    if package.weight <= truck_free_space:
                        self.truck_storage.append(package)
                        self.destination_ASP.remove(package)

            elif start_destination == Destination.DAR and end_destination == Destination.PER:
                for package in self.destination_PER:
                    if package.weight <= truck_free_space:
                        self.truck_storage.append(package)
                        self.destination_DAR.remove(package)

            elif start_destination == Destination.DAR and end_destination == Destination.ADL:
                for package in self.destination_ADL:
                    if package.weight <= truck_free_space:
                        self.truck_storage.append(package)
                        self.destination_ADL.remove(package)

            elif start_destination == Destination.DAR and end_destination == Destination.MEL:
                for package in self.destination_MEL:
                    if package.weight <= truck_free_space:
                        self.truck_storage.append(package)
                        self.destination_MEL.remove(package)

            elif start_destination == Destination.DAR and end_destination == Destination.SYD:
                for package in self.destination_SYD:
                    if package.weight <= truck_free_space:
                        self.truck_storage.append(package)
                        self.destination_SYD.remove(package)

            elif start_destination == Destination.DAR and end_destination == Destination.BRI:
                for package in self.destination_BRI:
                    if package.weight <= truck_free_space:
                        self.truck_storage.append(package)
                        self.destination_BRI.remove(package)

        return self.truck_storage