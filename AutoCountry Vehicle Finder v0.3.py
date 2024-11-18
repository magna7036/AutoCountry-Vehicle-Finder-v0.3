class CarFinder:
    def __init__(self):
        self.AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

    def print_all_allowed_vehicles(self):
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for vehicle in self.AllowedVehiclesList:
            print(vehicle)

    def search_vehicle(self, vehicle_name):
        if vehicle_name in self.AllowedVehiclesList:
            print(f"{vehicle_name} is an authorized vehicle.")
        else:
            print(f"{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again.")

    def add_vehicle(self, vehicle_name):
        if vehicle_name not in self.AllowedVehiclesList:
            self.AllowedVehiclesList.append(vehicle_name)
            print(f"{vehicle_name} has been added to the list of authorized vehicles.")
        else:
            print(f"{vehicle_name} is already in the list of authorized vehicles.")

def main():
    car_finder = CarFinder()

    while True:
        print("********************************")
        print("AutoCountry Vehicle Finder v0.3") 
        print("********************************")    
        print("Please Enter the following number below from the following menu:")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. Exit")
        choice = input("Please enter the full Vehicle name would you like to add: ")

        if choice == '1':
            car_finder.print_all_allowed_vehicles()
        elif choice == '2':
            vehicle_name = input("Please Enter the full Vehicle name: ")
            car_finder.search_vehicle(vehicle_name)
        elif choice == '3':
            vehicle_name = input("Please Enter the full Vehicle name you would like to add: ")
            car_finder.add_vehicle(vehicle_name)
        elif choice == '4':
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
