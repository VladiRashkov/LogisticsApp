from core.application_data import ApplicationData
from models.constants.truck_status import TruckStatus
from models.truck import Truck
from models.constants.truck_type import TruckType


class ShowTrucks:
    
    def __init__(self, params, app_data = ApplicationData):
        self._app_data = app_data
        self._params = params

       

    def execute(self): #shows all trucks in our system
        truck = Truck
        self._app_data.show_trucks()


    