from car import Car
from datetime import date
from engine  import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import SpindlerBattery, NubbinBattery

class CarFactory:
    @classmethod
    def create_calliope(cls, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(
            CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(current_date, last_service_date))
    
    @classmethod
    def create_glissade(cls, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            SpindlerBattery(current_date, last_service_date))

    @classmethod
    def create_palindrome(cls, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(
            SternmanEngine(current_mileage, last_service_mileage),
            SpindlerBattery(current_date, last_service_date))

    @classmethod
    def create_rorschach(cls, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(current_date, last_service_date))

    @classmethod
    def create_thovex(cls, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(
            CapuletEngine(current_mileage, last_service_mileage),
            NubbinBattery(current_date, last_service_date))