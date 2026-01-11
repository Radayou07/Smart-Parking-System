from parking_spot.parking_spot import ParkingSpot
from vehicle import VehicleSize, Vehicle

class CompactSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id, VehicleSize.COMPACT)

    def can_fit(self, vehicle: Vehicle):
        if vehicle.size != VehicleSize.COMPACT:
            print(f"Spot {self.id} is for compact vehicle only")
            return False
        return True

