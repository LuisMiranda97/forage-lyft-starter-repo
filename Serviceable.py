from abc import abstractmethod


from abc import ABC, abstractmethod

@abstractmethod
class Serviceable(ABC):
    def needs_service(self) -> bool:
        pass