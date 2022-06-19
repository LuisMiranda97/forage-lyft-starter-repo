from datetime import date
import Engine
import Battery
import Tire
from Car import Car

class CarFactory:
    @classmethod
    def create_calliope(cls, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int, tire_sensors : list) -> Car:
        return Car(
            Engine.CapuletEngine(last_service_mileage,current_mileage),
            Battery.SpindlerBattery(last_service_date, current_date),
            Tire.CarriganTire(tire_sensors))
            
    
    @classmethod
    def create_glissade(cls, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int, tire_sensors : list) -> Car:
        return Car(
            Engine.WilloughbyEngine(last_service_mileage,current_mileage),
            Battery.SpindlerBattery(last_service_date,current_date),
            Tire.OctoprimeTire(tire_sensors))

    @classmethod
    def create_palindrome(cls, current_date : date, last_service_date : date, warning_light_on : bool, tire_sensors : list) -> Car:
        return Car(
            Engine.SternmanEngine(warning_light_on),
            Battery.SpindlerBattery(last_service_date,current_date),
            Tire.CarriganTire(tire_sensors))

    @classmethod
    def create_rorschach(cls, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int, tire_sensors : list) -> Car:
        return Car(
            Engine.WilloughbyEngine(last_service_mileage, current_mileage),
            Battery.NubbinBattery(last_service_date, current_date),
            Tire.OctoprimeTire(tire_sensors))

    @classmethod
    def create_thovex(cls, current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int, tire_sensors : list) -> Car:
        return Car(
            Engine.CapuletEngine(last_service_mileage,current_mileage),
            Battery.NubbinBattery(last_service_date,current_date),
            Tire.CarriganTire(tire_sensors))