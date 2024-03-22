import Distance
import HashTable
import Package
import AddTimes
from datetime import time
#truck class holds truck variables and related functions, including deliver, which determins the trucks route in delivering packages
class Truck:
    def __init__(self, number):
        self.number = number
        self.capacity = 16
        self.inventory = []
        self.miles = 0
        self.departure_time = None
        self.return_time = None
        self.report = None

    def __str__(self):
        return f"Truck number {self.number}"
    #sets the trucks inventory to a given list so long as it does not exceed its capacity
    def load(self, id_list):
        if len(id_list) <= self.capacity:
            self.inventory = id_list
        else:
            print("List exceeds capacity")
    #self adjusting function that delivers all packages corrisponding to ids in inventory
    #counts milage and updates package information
    def deliver(self, start_address, start_time, hash_table):
        hash_table = hash_table
        #updates package status of all packages on the truck
        for id in self.inventory:
            (hash_table.search(id)).update_status(f"Package En Route")
            (hash_table.search(id)).update_left_hub_time(start_time)
            (hash_table.search(id)).update_truck_number(self.number)

        current_address = start_address
        next_package_id = None
        #as long as the truck is not empty, it will continue comparing distances and delivering the package with the smallest corisponding distance
        while len(self.inventory) > 0:
            current_min = 999999
            for item in self.inventory: #every package remaining in the truck is compared against the current address
                package_address = (hash_table.search(item)).get_address()
                distance = Distance.get_distance(current_address, package_address)
                if distance < current_min:
                    current_min = distance
                    next_package_id = item
            # moves truck to next(closest) address and updates mileage
            current_address = (hash_table.search(next_package_id)).get_address()
            self.miles += current_min
            # updates the package delvery time
            time_en_route_decimal = (self.miles / 18)
            total_min_en_route = int((time_en_route_decimal * 60) // 1)
            time_en_route = time((total_min_en_route // 60), (total_min_en_route % 60))
            delivery_time = AddTimes.add(start_time, time_en_route)
            (hash_table.search(next_package_id)).update_time(delivery_time)
            #updates package delivery status
            (hash_table.search(next_package_id)).update_status(f"Package Delivered by Truck #{self.number} at {delivery_time}")
            #removes delivered package from truck inventory
            self.inventory.remove(next_package_id)
        #when empty, the truck returns to the starting address and updates it miles and time
        return_distance = Distance.get_distance(current_address, start_address)
        self.miles += return_distance
        self.miles = round(self.miles, 2)
        current_address = start_address
        route_time = self.miles / 18
        total_min = int(route_time * 60)
        total_time = time((total_min // 60), (total_min % 60))
        self.return_time = AddTimes.add(start_time, total_time)
        self.report = f"Truck #{self.number} left at {start_time} and returned at {self.return_time} with {self.miles} total miles."
    #returns truck miles
    def get_miles(self):
        return self.miles
    #returns truck report
    def get_report(self):
        return self.report