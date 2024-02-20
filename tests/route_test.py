import unittest
from models.route import Route
from datetime import datetime, timedelta
from models.location import Location
from models.status import RouteStatus
from models.package import Package
from models.truck import Truck

class Route_Should(unittest.TestCase):
    def test_constructor_createsRoute_whenArgumentsAreValid(self):
        self.location1 = Location()
        self.location2 = Location()
        self.location3 = Location()

    def test_constructor(self):
        start_location = "Melbourne"
        other_locations = ("Sydney", "Bristbane")
        route = Route(start_location, *other_locations)

        # Asserting start_location and other_locations are set correctly
        self.assertEqual(route._start_location, start_location)
        self.assertEqual(route._other_locations, other_locations)

        # Asserting id is set correctly
        self.assertEqual(route._id, 1)

        # Asserting start_date_time is set correctly
        expected_start_date_time = datetime.today().replace(hour=6, minute=00, microsecond=00) + timedelta(days=1)
        self.assertEqual(route._start_date_time, expected_start_date_time)

        # Asserting status is set correctly
        self.assertEqual(route._status, RouteStatus.OPEN)

        # Asserting packages and truck are initialized correctly
        self.assertEqual(route._packages, [])
        self.assertIsNone(route._truck)
