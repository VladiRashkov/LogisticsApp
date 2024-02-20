import unittest
from models.status import PackageStatus
from datetime import datetime
from models.package import Package

class Package_Should(unittest.TestCase):
    def test_package_creation(self):
        # Arrange
        start = "Perth"
        end = "Sydney"
        weight = 13
        username = "johndoe"

        # Act
        package = Package(start, end, weight, username)

        # Assert
        self.assertEqual(package.start, start)
        self.assertEqual(package.end, end)
        self.assertEqual(package.weight, weight)
        self.assertEqual(package.status, PackageStatus.UNASSIGNED)
        self.assertEqual(package.username, username)
        self.assertIsInstance(datetime.strptime(package.date, '%d/%m %A @ %H:%M'), datetime)