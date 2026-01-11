from parking_system import ParkingSystem
from vehicle import Vehicle, VehicleSize

def select_vehicle_size():
    print("Select vehicle size:")
    print("1. Compact")
    print("2. Medium")
    print("3. Large")
    choice = input("Enter choice (1-3): ")
    if choice == "1":
        return VehicleSize.COMPACT
    elif choice == "2":
        return VehicleSize.MEDIUM
    elif choice == "3":
        return VehicleSize.LARGE
    else:
        print("Invalid choice, defaulting to Compact")
        return VehicleSize.COMPACT

def main():
    print("#" * 60)
    print(" " * 20 + "SMART PARKING SYSTEM")
    print("#" * 60)

    system = ParkingSystem()

    while True:
        print("\nMenu:")
        print("1. Park Vehicle")
        print("2. Exit Vehicle")
        print("3. Reserve Spot")
        print("4. Park Reserved Vehicle")
        print("5. Show Parking Status")
        print("6. Exit Program")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            license_plate = input("Enter vehicle license plate: ")
            size = select_vehicle_size()
            vehicle = Vehicle(license_plate, size)
            system.park_vehicle(vehicle)

        elif choice == "2":
            license_plate = input("Enter vehicle license plate to exit: ")
            system.exit_vehicle(license_plate)

        elif choice == "3":
            spot_id = input("Enter spot ID to reserve: ")
            license_plate = input("Enter vehicle license plate for reservation: ")
            system.reserve_spot(spot_id, license_plate)

        elif choice == "4":
            license_plate = input("Enter reserved vehicle license plate: ")
            size = select_vehicle_size()
            system.park_reserve_spot(license_plate, size)

        elif choice == "5":
            system.show_status()

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
