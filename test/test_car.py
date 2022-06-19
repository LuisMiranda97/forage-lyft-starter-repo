import unittest
from datetime import datetime
import Battery
import Engine
from CarFactory import CarFactory

class TestBattery(unittest.TestCase):
    def test_spindler_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        spindler = Battery.SpindlerBattery(last_service_date,today)

        self.assertTrue(spindler.needs_service())
    
    def test_spindler_not_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        spindler = Battery.SpindlerBattery(last_service_date,today)

        self.assertFalse(spindler.needs_service())
    
    def test_nubbin_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        nubbin = Battery.NubbinBattery(last_service_date,today)

        self.assertTrue(nubbin.needs_service())
    
    def test_nubbin_not_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        nubbin = Battery.NubbinBattery(last_service_date,today)

        self.assertFalse(nubbin.needs_service())

class TestEngine(unittest.TestCase):
    def test_sternman_needs_service(self):
        warning_light_on = True
        sternman = Engine.SternmanEngine(warning_light_on)

        self.assertTrue(sternman.needs_service())

    def test_sternman_not_needs_service(self):
        warning_light_on = False
        sternman = Engine.SternmanEngine(warning_light_on)

        self.assertFalse(sternman.needs_service())

    def test_capulet_needs_service(self):
        last_service_mileage = 0
        current_mileage = 30000
        capulet = Engine.CapuletEngine(last_service_mileage,current_mileage)

        self.assertTrue(capulet.needs_service())
    
    def test_capulet_not_needs_service(self):
        last_service_mileage = 0
        current_mileage = 20000
        capulet = Engine.CapuletEngine(last_service_mileage,current_mileage)

        self.assertFalse(capulet.needs_service())
    
    def test_willoughby_needs_service(self):
        last_service_mileage = 0
        current_mileage = 60000
        willoughby = Engine.WilloughbyEngine(last_service_mileage,current_mileage)

        self.assertTrue(willoughby.needs_service())
    
    def test_willoughby_not_needs_service(self):
        last_service_mileage = 0
        current_mileage = 50000
        willoughby = Engine.WilloughbyEngine(last_service_mileage,current_mileage)

        self.assertFalse(willoughby.needs_service())

class TestCarFactory(unittest.TestCase):
    # Calliope Factory
    def test_calliope_needs_service_from_engine(self):
        last_service_mileage = 0
        current_mileage = 30000
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        calliope = CarFactory.create_calliope(today,last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(calliope.needs_service())
    
    def test_calliope_needs_service_from_battery(self):
        last_service_mileage = 0
        current_mileage = 20000
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        calliope = CarFactory.create_calliope(today,last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(calliope.needs_service())

    def test_calliope_not_needs_service(self):
        last_service_mileage = 0
        current_mileage = 20000
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        calliope = CarFactory.create_calliope(today,last_service_date,current_mileage,last_service_mileage)

        self.assertFalse(calliope.needs_service())
    
    # Glissade Factory
    def test_glissade_needs_service_from_engine(self):
        last_service_mileage = 0
        current_mileage = 60000
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        glissade = CarFactory.create_glissade(today,last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(glissade.needs_service())
    
    def test_glissade_needs_service_from_battery(self):
        last_service_mileage = 0
        current_mileage = 50000
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        glissade = CarFactory.create_glissade(today,last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(glissade.needs_service())

    def test_glissade_not_needs_service(self):
        last_service_mileage = 0
        current_mileage = 50000
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        glissade = CarFactory.create_glissade(today,last_service_date,current_mileage,last_service_mileage)

        self.assertFalse(glissade.needs_service())

    # Glissade Factory
    def test_glissade_needs_service_from_engine(self):
        last_service_mileage = 0
        current_mileage = 60000
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        glissade = CarFactory.create_glissade(today,last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(glissade.needs_service())
    
    def test_glissade_needs_service_from_battery(self):
        last_service_mileage = 0
        current_mileage = 50000
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        glissade = CarFactory.create_glissade(today,last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(glissade.needs_service())

    def test_glissade_not_needs_service(self):
        last_service_mileage = 0
        current_mileage = 50000
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        glissade = CarFactory.create_glissade(today,last_service_date,current_mileage,last_service_mileage)

        self.assertFalse(glissade.needs_service())

    # Palindrome Factory
    def test_palindrome_needs_service_from_engine(self):
        warning_light_on = True
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        palindrome = CarFactory.create_palindrome(today,last_service_date,warning_light_on)

        self.assertTrue(palindrome.needs_service())
    
    def test_palindrome_needs_service_from_battery(self):
        warning_light_on = False
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        palindrome = CarFactory.create_palindrome(today,last_service_date,warning_light_on)

        self.assertTrue(palindrome.needs_service())

    def test_palindrome_not_needs_service(self):
        warning_light_on = False
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        palindrome = CarFactory.create_palindrome(today,last_service_date,warning_light_on)

        self.assertFalse(palindrome.needs_service())
    
    # Rorschach Factory
    def test_rorschach_needs_service_from_engine(self):
        last_service_mileage = 0
        current_mileage = 60000
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        rorschach = CarFactory.create_rorschach(today,last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(rorschach.needs_service())
    
    def test_rorschach_needs_service_from_battery(self):
        last_service_mileage = 0
        current_mileage = 50000
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        rorschach = CarFactory.create_rorschach(today,last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(rorschach.needs_service())

    def test_rorschach_not_needs_service(self):
        last_service_mileage = 0
        current_mileage = 50000
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        rorschach = CarFactory.create_rorschach(today,last_service_date,current_mileage,last_service_mileage)

        self.assertFalse(rorschach.needs_service())

    # Thovex Factory
    def test_thovex_needs_service_from_engine(self):
        last_service_mileage = 0
        current_mileage = 30000
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        thovex = CarFactory.create_thovex(today,last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(thovex.needs_service())
    
    def test_thovex_needs_service_from_battery(self):
        last_service_mileage = 0
        current_mileage = 20000
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        thovex = CarFactory.create_thovex(today,last_service_date,current_mileage,last_service_mileage)

        self.assertTrue(thovex.needs_service())

    def test_thovex_not_needs_service(self):
        last_service_mileage = 0
        current_mileage = 20000
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        thovex = CarFactory.create_thovex(today,last_service_date,current_mileage,last_service_mileage)

        self.assertFalse(thovex.needs_service())
    

if __name__ == '__main__':
    unittest.main()
