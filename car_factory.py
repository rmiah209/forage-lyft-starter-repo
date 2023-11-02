from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class CarFactory:
    def create_calliope(
        current_date,
        last_service_date,
        current_mileage,
        last_service_mileage,
        tire_wear,
    ):
        engine = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        battery = NubbinBattery(
            current_date=current_date, last_service_date=last_service_date
        )

        tire = CarriganTire(tire_wear=tire_wear)

        car = Car(engine, battery, tire)

        return car

    def create_glissade(
        current_date,
        last_service_date,
        current_mileage,
        last_service_mileage,
        tire_wear,
    ):
        engine = WilloughbyEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage
        )

        battery = SpindlerBattery(current_date, last_service_date)

        tire = OctoprimeTire(tire_wear=tire_wear)

        car = Car(engine, battery, tire)

        return car

    def create_palindrome(
        current_date, last_service_date, warning_light_is_on, tire_wear
    ):
        engine = SternmanEngine(warning_light_is_on)

        battery = SpindlerBattery(current_date, last_service_date)

        tire = CarriganTire(tire_wear=tire_wear)

        car = Car(engine, battery, tire)

        return car

    def create_rorschach(
        current_date,
        last_service_date,
        current_mileage,
        last_service_mileage,
        tire_wear,
    ):
        engine = WilloughbyEngine(
            last_service_mileage=last_service_mileage, current_mileage=current_mileage
        )

        battery = SpindlerBattery(current_date, last_service_date)

        tire = OctoprimeTire(tire_wear=tire_wear)

        car = Car(engine, battery, tire)

        return car

    def create_thovex(
        current_date,
        last_service_date,
        current_mileage,
        last_service_mileage,
        tire_wear,
    ):
        engine = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )

        battery = NubbinBattery(
            current_date=current_date, last_service_date=last_service_date
        )

        tire = OctoprimeTire(tire_wear=tire_wear)

        car = Car(engine, battery, tire)

        return car
