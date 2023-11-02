import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_capulet_engine_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)

        self.assertTrue(engine.needs_service())

    def test_capulet_engine_should_not_need_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)

        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_sternman_engine_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        warning_light = True

        engine = SternmanEngine(last_service_date, warning_light)

        self.assertTrue(engine.needs_service())

    def test_sternman_engine_should_not_need_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        warning_light = False

        engine = SternmanEngine(last_service_date, warning_light)

        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_willoughby_engine_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        engine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage
        )

        self.assertTrue(engine.needs_service())
