from parking_state.parking_state import ParkingSpotState
class OccupiedState(ParkingSpotState):
    def __init__(self, spot):
        self.spot = spot

    def park(self, spot, vehicle):
        print(f"Spot {spot.id} is already occupied")
        return False

    def exit(self, spot): #behavior of exit park
        spot.vehicle = None
        spot.is_occupied = False
        from parking_state.available_state import AvailableState
        spot.state = AvailableState(spot)
        print(f"Vehicle exited from spot {spot.id}")
        return True

    def get_state_name(self):
        return "Occupied"


