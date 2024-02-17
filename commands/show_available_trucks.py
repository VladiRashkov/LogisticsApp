# checks capacity and the range
# and print the options 
# if a truck is found return the first id of the type of truck that meets the requirements

from core.application_data import ApplicationData
from models.truck import Truck
from models.constants.truck_status import TruckStatus


class ShowAvailableTrucks: #shows available trucks for route
        def __init__(self, params, app_data = ApplicationData):
                self.params = params
                self.app_data = app_data

        def execute(self):      #(package_weight, range)
                
                available_trucks = []
                for truck in self.app_data._trucks:
                        if not TruckStatus.FREE:
                                raise ValueError(f'Truck with {truck.id} is Busy')
                        # if truck.free_capacity > package_weight:
                        #         pass #logic for loading the truck or select the truck
                        #         if truck.range > routes.distance:
                        #                 pass # logic for routes.distance/km 
                        available_trucks.append(truck.id) #not sure about the truck.id how should it work
                        
                for truck in available_trucks:
                        
                        print(truck.to_string)

        def available_to_string(self):
                pass
        # def calculate_free_space(self):
        #         pass
        # def calculate_range(self) -> bool:
        #         pass
                