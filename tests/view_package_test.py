import unittest
from datetime import datetime
from core.application_data import ApplicationData
from models.package import Package
from commands.view_package import ViewPackage
 
class ViewPackage_Should(unittest.TestCase):
    def setUp(self):
        self.package1 = Package("Perth", "Brisbain", 10, "user1")
        self.package2 = Package("Sydney", "Melbourne", 20, "user2")
        self.package3 = Package("Darwin", "Perth", 30, "User3")
        
        self.app_data = ApplicationData()
        self.app_data.packages = [self.package1, self.package2, self.package3]
    
    
    def test_view_unassigned_packages(self):
        view_package = ViewPackage(["Unassigned"], self.app_data)
        result = view_package.execute()
        self.assertIn(str(self.package1), result)
        self.assertIn(str(self.package2), result)
        self.assertIn(str(self.package3), result)

    def test_view_assigned_packages(self):
       

        view_package = ViewPackage(["Assigned"], self.app_data)
        result = view_package.execute()
        self.assertIn(str(self.package1), result)
        self.assertIn(str(self.package2), result)
        self.assertIn(str(self.package3), result)

    def test_view_in_progress_packages(self):
      
        view_package = ViewPackage(["In progress"], self.app_data)
        result = view_package.execute()
        self.assertIn(str(self.package1), result)
        self.assertIn(str(self.package2), result)
        self.assertIn(str(self.package3), result)

    def test_view_delivered_packages(self):
        

        view_package = ViewPackage(["Delivered"], self.app_data)
        result = view_package.execute()
        self.assertIn(str(self.package1), result)
        self.assertIn(str(self.package2), result)
        self.assertIn(str(self.package3), result)