from parking_lot import ParkingLot
from parking_spot.compact_spot import CompactSpot
from parking_spot.large_spot import LargeSpot
from parking_spot.parking_spot import ParkingSpot
from vehicle import Vehicle, VehicleSize

class ParkingSystem:
    def __init__(self):
        self.parking_lot = ParkingLot("Downtown Parking")
        self._initialize_parking_lot()

    def _initialize_parking_lot(self):
        for i in range(1, 4):
            self.parking_lot.add_spot(CompactSpot(f"C{i}"))
        for i in range(1, 3):
            self.parking_lot.add_spot(ParkingSpot(f"M{i}", VehicleSize.MEDIUM))
        for i in range(1, 3):
            self.parking_lot.add_spot(LargeSpot(f"L{i}"))

    def park_vehicle(self, vehicle: Vehicle):
        print(f"\nAttempting to park {vehicle}...")
        spot = self.parking_lot.find_available_spot(vehicle) # Check available spot: spot -> ParkingSpot or spot->None
        if spot and spot.park_vehicle(vehicle): 
            print(f"✓ Parked {vehicle.license_plate} in spot {spot.id}")
            return True
        print(f"✗ No available spot for {vehicle}")
        return False

    def exit_vehicle(self, license_plate: str):
        print(f"\nVehicle {license_plate} exiting...")
        spot = self.parking_lot.find_vehicle(license_plate) # spot → ParkingSpot object (ex: c1:[id,state]) or spot->None
        if spot and spot.exit_vehicle(): # spot.exit_vehicle() moves to ParkingSpot class
            print(f"✓ Vehicle {license_plate} exited from spot {spot.id}")
            return True
        print(f"✗ Vehicle {license_plate} not found")
        return False

    def reserve_spot(self, spot_id: str, license_plate: str):
        for spot in self.parking_lot.spots:
            if spot.id == spot_id:
                if spot.reserve(license_plate):
                    print(f"✓ Spot {spot_id} reserved for {license_plate}")
                    return True
                print(f"✗ Spot {spot_id} cannot be reserved")
                return False
        print(f"✗ Spot {spot_id} not found")
        return False

    #write by own 
    def park_reserve_spot(self, license_plate: str, size: VehicleSize):
        print(f"\nVehicle {license_plate} parking (reserved)...")
        # Find reserved spot
        spot = self.parking_lot.find_reserved_spot(license_plate)
        if not spot:
            print(f"✗ No reserved spot for {license_plate}")
            return False
        # Create vehicle
        vehicle = Vehicle(license_plate, size)
        # Let the spot handle parking (State Pattern)
        if spot.park_vehicle(vehicle):
            print(f"✓ Vehicle {license_plate} parked in reserved spot {spot.id}")
            return True
        print(f"✗ Failed to park reserved vehicle {license_plate}")
        return False

        
    def show_status(self):
        self.parking_lot.display_status()


