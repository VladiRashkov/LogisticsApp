class BaseHub:
    def __init__(self, total_weight: int):
        self._total_weight = total_weight
        # self._storage = []
    
    @property
    def total_weight(self):
        return self._total_weight
    
    # @property
    # def storage(self):
    #     return tuple(self._storage)
     
    def add_package_to_storage(self, destination, package):
        pass

    def load_truck_remove_packages(self, truck_free_space, start_destination, end_destination):
        pass

    def view(self):
        pass
    
    def __str__(self) -> str:
        pass