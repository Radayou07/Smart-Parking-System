from typing import List, Optional
from parking_spot.parking_spot import ParkingSpot
from vehicle import Vehicle
from parking_state.available_state import AvailableState
from parking_state.occupied_state import OccupiedState
from parking_state.reserved_state import ReservedState

class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots: List[ParkingSpot] = []

    def add_spot(self, spot: ParkingSpot):
        self.spots.append(spot)

    def find_available_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]: 
        for spot in self.spots:
            if isinstance(spot.state, AvailableState) and spot.can_fit(vehicle):
                return spot
        return None

    def find_vehicle(self, license_plate: str) -> Optional[ParkingSpot]:    #If found → return the ParkingSpot
                                                                            #If not found → return None
        for spot in self.spots:
            if spot.vehicle and spot.vehicle.license_plate == license_plate: # spot.vehicle: ensure spot not empty, prevent None.license_plate
                return spot # Returns the ParkingSpot object include (spot_id, state = occupied,information vehicle),spot → ParkingSpot
        return None# spot->None
    
    def find_reserved_spot(self, license_plate: str):
        for spot in self.spots:
            if (
                hasattr(spot.state, "reserved_for")
                and spot.state.reserved_for == license_plate
            ):
                return spot
        return None


    def get_available_count(self):
        return sum(1 for spot in self.spots if isinstance(spot.state, AvailableState))

    def get_occupied_count(self):
        return sum(1 for spot in self.spots if isinstance(spot.state, OccupiedState))

    def get_reserved_count(self):
        return sum(1 for spot in self.spots if isinstance(spot.state, ReservedState ))
    
    def display_status(self):
        print(f"\nParking Lot: {self.name}")
        for spot in self.spots:
            print(f"  {spot}")
        print(f"Available: {self.get_available_count()} | Occupied: {self.get_occupied_count()} | Reserved: {self.get_reserved_count()}\n")