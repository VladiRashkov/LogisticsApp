class BaseHub:
    def __init__(self, city_name: str, storage_kg: int):
        self._city_name = city_name
        self._storage_kg = storage_kg
        # self._storage = []
    @property
    def city_name(self):
        return self._city_name
    
    @property
    def storage_kg(self):
        return self._storage_kg
    
    # @property
    # def storage(self):
    #     return tuple(self._storage)
     
    def add_package_to_storage(self, destination, package):
        pass

    def load_truck_remove_packages(self, truck_free_space, start_destination, end_destination):
        pass

    def load_truck(self):
        pass

    def view(self):
        #return '\n'.join([f'{self}'] + [f'  {package}' for package in self._storage]) #? self? v nachaloto?
        pass
    def __str__(self) -> str:
        #return f'#{self.id}. {self.name_package} ({len(self._storage)} kg)' #? self? id v nachaloto?
        pass