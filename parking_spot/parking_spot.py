from vehicle import Vehicle, VehicleSize
from parking_state.available_state import AvailableState
from parking_state.reserved_state import ReservedState

class ParkingSpot:
    def __init__(self, spot_id, size: VehicleSize): # spot is object of ParkingSpot,spot has it own atributes
        self.id = spot_id
        self.size = size
        self.is_occupied = False
        self.vehicle = None
        self.state = AvailableState(self)

    def can_fit(self, vehicle: Vehicle):
        return vehicle.size.value <= self.size.value 

    def park_vehicle(self, vehicle: Vehicle):
        return self.state.park(self, vehicle)

    def exit_vehicle(self):
        return self.state.exit(self)
        # `self.state.exit(self)` is calling the `exit` method of the current state object that
        # is associated with the parking spot. This method is responsible for handling the
        # logic when a vehicle exits the parking spot. The `self` parameter is passed to the
        # `exit` method to provide a reference to the current `ParkingSpot` object on which the
        # method is being called.
        

    def reserve(self, license_plate: str):
        if isinstance(self.state, AvailableState):
            self.state = ReservedState(self, license_plate)
            return True
        return False
    
    
    
    # def reserve(self, vehicle):
    # # from parking_state.available_state import AvailableState
    # # from parking_state.reserved_state import ReservedState

    #     if isinstance(self.state, AvailableState) and self.can_fit(vehicle):
    #         self.state = ReservedState(self, vehicle.license_plate, vehicle.size)
    #         return True
    #     return False




    def get_state_name(self):
        return self.state.get_state_name()

    def __str__(self):
        vehicle_info = f"[{self.vehicle.license_plate}]" if self.vehicle else ""
        return f"Spot {self.id} ({self.size.name}) - {self.get_state_name()} {vehicle_info}"



