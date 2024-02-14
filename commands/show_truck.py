# checks capacity and the range
# and print the options 
# if a truck is found return the first id of the type of truck that meets the requirements

from core.application_data import ApplicationData
from models.truck import Truck


class Truck_Info:
        def __init__(self, params, app_data = ApplicationData):
                self.params = params
                self.app_data = app_data

        def execute(self, package_weight, routes):
                available_trucks = []
                for truck in self.app_data._trucks:
                        if truck.free_capacity > package_weight:
                                pass #logic for loading the truck or select the truck
                        if truck.range > routes.distance:
                                pass # logic for routes.distance/km 
                        available_trucks.append(truck.id) #not sure about the truck.id how should it work
                        
                for truck in available_trucks:
                        print(f'{truck.id}, {truck.name} \n {truck.capacity}, {truck.range}\n is available for this route!')

                