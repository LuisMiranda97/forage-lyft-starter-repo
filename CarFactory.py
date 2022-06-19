from datetime import date
import Engine
import Battery
from Car import Car

class CarFactory:
    @classmethod
    def create_calliope(cls, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(
            Engine.CapuletEngine(last_service_mileage,current_mileage),
            Battery.SpindlerBattery(last_service_date, current_date))
    
    @classmethod
    def create_glissade(cls, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(
            Engine.WilloughbyEngine(last_service_mileage,current_mileage),
            Battery.SpindlerBattery(last_service_date,current_date))

    @classmethod
    def create_palindrome(cls, current_date : date, last_service_date : date, warning_light_on : bool) -> Car:
        return Car(
            Engine.SternmanEngine(warning_light_on),
            Battery.SpindlerBattery(last_service_date,current_date))

    @classmethod
    def create_rorschach(cls, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(
            Engine.WilloughbyEngine(last_service_mileage, current_mileage),
            Battery.NubbinBattery(last_service_date, current_date))

    @classmethod
    def create_thovex(cls, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(
            Engine.CapuletEngine(last_service_mileage,current_mileage),
            Battery.NubbinBattery(last_service_date,current_date))