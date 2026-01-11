from enum import Enum

class VehicleSize(Enum):
    COMPACT = 1
    MEDIUM = 2
    LARGE = 3

class Vehicle:
    """Represents a vehicle trying to park"""
    def __init__(self, license_plate: str, size: VehicleSize):
        self.license_plate = license_plate
        self.size = size

    def __str__(self):
        return f"Vehicle({self.license_plate}, {self.size.name})"
