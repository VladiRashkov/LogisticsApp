from core.application_data import ApplicationData

class ViewRouteCommand:
    def __init__(self, params: list[str], app_data: ApplicationData):
        self._params = params
        self._app_data = app_data

    def execute(self):
        pass