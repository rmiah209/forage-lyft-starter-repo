from abc import ABC


class Tire(ABC):
    @abstractclassmethod
    def needs_service(self):
        pass
