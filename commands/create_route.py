from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from commands.base_command import BaseCommand

class CreateRouteCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData, models_factory: ModelsFactory):
        super().__init__(params, app_data)
        self._models_factory = models_factory

    def execute(self):
        start_location = self.params[0]
        other_locations = self.params[1:]

        route = self._models_factory.create_route(start_location, *other_locations)
        self.app_data.add_route(route)

        return f'Route with ID: {route.id} has been created!'


# Input: CreateRoute AliceSprings Adelaide Sydney Melbourne Bristbane (n params)
# Output: Route with ID: 1 has been created!
