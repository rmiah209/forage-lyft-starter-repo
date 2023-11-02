import unittest
from datetime import datetime

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def should_need_service(self):
        tire_wear = [0, 0, 0.9, 0]

        tire = CarriganTire(tire_wear)

        self.assertTrue(tire.needs_service())

    def should_not_need_service(self):
        tire_wear = [0, 0, 0, 0]

        tire = CarriganTire(tire_wear)

        self.assertFalse(tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def should_need_service(self):
        tire_wear = [1, 1, 1, 0]

        tire = OctoprimeTire(tire_wear)

        self.assertTrue(tire.needs_service())

    def should_not_need_service(self):
        tire_wear = [1, 0, 1, 0]

        tire = OctoprimeTire(tire_wear)

        self.assertFalse(tire.needs_service())


if __name__ == "__main__":
    unittest.main()
