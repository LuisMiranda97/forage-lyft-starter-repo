from Battery import Battery
from Engine import Engine
from Serviceable import Serviceable
from Tire import Tire

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
