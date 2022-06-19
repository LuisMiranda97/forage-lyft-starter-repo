from Serviceable import Serviceable
from dateutil import relativedelta
from datetime import datetime

class Battery(Serviceable):
    pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        diff = relativedelta.relativedelta(self.current_date, self.last_service_date)
        return  diff.years >= 2

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        diff = relativedelta.relativedelta(self.current_date, self.last_service_date)
        return  diff.years >= 4


today = datetime.today().date()
last_service_date = today.replace(year=today.year - 1)
spindler = SpindlerBattery(last_service_date,today)
