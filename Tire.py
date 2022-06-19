from Serviceable import Serviceable

class Tire(Serviceable):
    pass

class CarriganTire(Tire):
    def __init__(self,sensors:list):
        self.sensors = sensors

    def needs_service(self) -> bool:
        for sensor in self.sensors:
            if sensor >= 0.9:
                return True
        return False
    
class OctoprimeTire(Tire):
    def __init__(self,sensors:list):
        self.sensors = sensors

    def needs_service(self) -> bool:
        return sum(self.sensors) >= 3
