# checks capacity and the range
# and print the options 
# if a truck is found return the first id of the type of truck that meets the requirements

from core.application_data import ApplicationData
from models.truck import Truck
from models.constants.truck_status import TruckStatus


class FindTrucks: #shows available trucks for route
        def __init__(self, params, app_data: ApplicationData):
                self.params = params
                self.app_data = app_data

        def execute(self):
                
                available_trucks = []
                
                for truck in self.app_data._trucks:
                        if truck._status != TruckStatus.FREE:
                                raise ValueError(f'Truck with {truck._truck_id} is Busy')
                        trucks = truck.to_string()
                        available_trucks.append(str(trucks))  
                trucks_str = '\n'.join(available_trucks)   
                print(f'Available trucks: {trucks_str}')