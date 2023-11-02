import unittest
from datetime import datetime

from battery.battery import Battery
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from tire.tire import Tire
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        battery = Battery(last_service_date, current_mileage, last_service_mileage)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        battery = Battery(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(battery.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        battery = NubbinBattery(current_date, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_should_not_need_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        battery = NubbinBattery(current_date, last_service_date)

        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_battery_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        battery = SpindlerBattery(current_date, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_not_need_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        battery = SpindlerBattery(current_date, last_service_date)

        self.assertFalse(battery.needs_service())


if __name__ == "__main__":
    unittest.main()
