from parking_state.parking_state import ParkingSpotState
from parking_state.occupied_state import OccupiedState

class AvailableState(ParkingSpotState):
    def __init__(self, spot):
        self.spot = spot

    def park(self, spot, vehicle):
        if spot.is_occupied:
            print(f"Spot {spot.id} is already occupied")
            return False
        spot.vehicle = vehicle
        spot.is_occupied = True
        spot.state = OccupiedState(spot)
        print(f"Vehicle {vehicle.license_plate} parked in spot {spot.id}")
        return True
    
    def exit(self, spot):
        print(f"Spot {spot.id} is already empty")
        return False

    def get_state_name(self):
        return "Available"

