from abc import ABC


class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass
