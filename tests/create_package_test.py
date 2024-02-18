import unittest
from core.application_data import ApplicationData
from commands.create_package import CreatePackageCommand
from models.package import Package

class CreatePackage_Should(unittest.TestCase):
    def test_execute(self):
        app_data = ApplicationData()

        params = ["Perth", "Sydney", 85, "jscully"]

        command = CreatePackageCommand(params, app_data)

        result = command.execute()
        
        package = app_data._packages[0]

        self.assertEqual(len(app_data.packages), 1)

        self.assertEqual(package.start, "Perth")
        self.assertEqual(package.end, "Sydney")
        self.assertEqual(package.weight, 85)
        self.assertEqual(package.status, "Unassigned")
        self.assertEqual(package.username, "jscully")
        
        expected_result = "Package 1 from Perth to Sydney of the jscully, 85 kg accepted in Perth Hub."
        self.assertEqual(result, expected_result)
