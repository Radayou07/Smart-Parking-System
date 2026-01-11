from parking_state.parking_state import ParkingSpotState
from parking_state.occupied_state import OccupiedState
# from vehicle import Vehicle, VehicleSize
class ReservedState(ParkingSpotState):
    def __init__(self, spot, reserved_for):
        self.spot = spot
        self.reserved_for = reserved_for
        # self.size = size

    def park(self, spot, vehicle):
        if vehicle.license_plate == self.reserved_for:# and vehicle.size == self.size:
            spot.vehicle = vehicle
            spot.is_occupied = True
            spot.state = OccupiedState(spot)
            print(f"VIP Vehicle {vehicle.license_plate} parked in reserved spot {spot.id}")
            return True
        print(f"Spot {spot.id} is reserved for {self.reserved_for}")
        return False

    def exit(self, spot):
        print(f"Spot {spot.id} is reserved and empty")
        return False

    def get_state_name(self):
        return f"Reserved (for {self.reserved_for})"



# from parking_state.parking_state import ParkingSpotState
# from parking_state.occupied_state import OccupiedState

# class ReservedState(ParkingSpotState):
#     def __init__(self, spot, reserved_for, reserved_size):
#         self.spot = spot
#         self.reserved_for = reserved_for      # license plate
#         self.reserved_size = reserved_size    # VehicleSize

#     def park(self, spot, vehicle):
#         # 1️⃣ Check license plate
#         if vehicle.license_plate != self.reserved_for:
#             print(f"Spot {spot.id} is reserved for {self.reserved_for}")
#             return False

#         # 2️⃣ Force reserved size (ignore wrong user input)
#         vehicle.size = self.reserved_size

#         # 3️⃣ Check if vehicle fits the spot
#         if not spot.can_fit(vehicle):
#             print(f"Vehicle size does not fit spot {spot.id}")
#             return False

#         # 4️⃣ Park successfully
#         spot.vehicle = vehicle
#         spot.is_occupied = True
#         spot.state = OccupiedState(spot)

#         print(f"Reserved vehicle {vehicle.license_plate} parked in spot {spot.id}")
#         return True

#     def exit(self, spot):
#         print(f"Spot {spot.id} is reserved and empty")
#         return False

#     def get_state_name(self):
#         return f"Reserved (for {self.reserved_for})"
