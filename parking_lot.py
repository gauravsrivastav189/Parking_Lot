class ParkingLot:
    def __init__(self):
        self.spots = {}
        self.total_spots = 40
        self.initialize_spots()

    def initialize_spots(self):
        for level in ["A", "B"]:
            for spot in range(1, 21):
                self.spots[level + str(spot)] = None

    def assign_spot(self, vehicle_number):
        last_4_digits = vehicle_number[-4:]
        for spot, status in self.spots.items():
            if status is None:
                self.spots[spot] = vehicle_number
                return {"level": spot[0], "spot": int(spot[1:])}
            elif status[-4:] == last_4_digits:
                return "Vehicle already parked"
        return "Sorry, the parking lot is full."


    def retrieve_spot(self, vehicle_number):
        for spot, v_number in self.spots.items():
            if v_number == vehicle_number:
                return {"level": spot[0], "spot": int(spot[1:])}
        return None

    def release_spot(self, vehicle_number):
        for spot, v_number in self.spots.items():
            if v_number == vehicle_number:
                self.spots[spot] = None
                return {"level": spot[0], "spot": int(spot[1:])}
        return None



def main():
    parking_lot = ParkingLot()
    while True:
        print("Main Menu:")
        print("1 - Enter the vehicle number to park")
        print("2 - Enter vehicle number to see where it is parked")
        print("3 - Enter vehicle number to release the parking spot")
        print("4 - Enter 'q' to quit")
        # print(parking_lot.spots)

        choice = input("Enter your choice: ").strip().lower()

        if choice == '1':
            vehicle_number = input("Enter the last 4 digits of your vehicle number: ").strip()
            result = parking_lot.assign_spot(vehicle_number)
            if isinstance(result, dict):
                print(f"Park your vehicle at Level {result['level']}, Spot {result['spot']}")
            else:
                print(result)
        elif choice == '2':
            vehicle_number = input("Enter the vehicle number: ").strip().upper()
            spot = parking_lot.retrieve_spot(vehicle_number)
            if spot:
                print(f"Vehicle with number {vehicle_number} is parked at Level {spot['level']}, Spot {spot['spot']}")
            else:
                print(f"Vehicle with number {vehicle_number} not found in the parking lot.")
        elif choice == '3':
            vehicle_number = input("Enter the vehicle number: ").strip().upper()
            released_spot = parking_lot.release_spot(vehicle_number)
            if released_spot:
                print(f"Vehicle with number {vehicle_number} released from Level {released_spot['level']}, Spot {released_spot['spot']}")
            else:
                print(f"Vehicle with number {vehicle_number} not found in the parking lot.")
        elif choice == '4':
            continue
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()



