from abc import ABC, abstractmethod

class ParkingSpotState(ABC):
    """Base class for all parking spot states"""

    @abstractmethod
    def park(self, spot, vehicle):
        pass

    @abstractmethod
    def exit(self, spot):
        pass

    @abstractmethod
    def get_state_name(self):
        pass
    