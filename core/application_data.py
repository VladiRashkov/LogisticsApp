from Models.Package import Package

class ApplicationData:
    def __init__(self):
        self._packages: list[Package] = []

    @property
    def packages(self):
        return tuple(self._packages)

    def add_package(self, package: Package):
        self._packages.append(package)