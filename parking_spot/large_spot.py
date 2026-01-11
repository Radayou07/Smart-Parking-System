from parking_spot.parking_spot import ParkingSpot
from vehicle import Vehicle, VehicleSize

class LargeSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id, VehicleSize.LARGE)

    def can_fit(self, vehicle: Vehicle):
        return True  # Large spots accept all vehicles

