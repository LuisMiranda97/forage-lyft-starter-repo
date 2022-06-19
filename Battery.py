from Serviceable import Serviceable
from dateutil import relativedelta
from datetime import datetime, date

class Battery(Serviceable):
    pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date:date, current_date:date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        diff = relativedelta.relativedelta(self.current_date, self.last_service_date)
        return  diff.years >= 3

class NubbinBattery(Battery):
    def __init__(self, last_service_date:date, current_date:date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        diff = relativedelta.relativedelta(self.current_date, self.last_service_date)
        return  diff.years >= 4

