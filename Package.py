from datetime import time
#package class to hold all package data and related functions
class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, special_notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight #in KG
        self.special_note = special_notes
        self.delivery_status = None
        self.left_hub_time = None
        self.delivery_time = None
        self.truck_number = None


    def __str__(self):
        return f"Package id:{self.id} - Delivery Address:{self.address} - Deadline:{self.deadline} - City:{self.city} - Zip Code:{self.zip} - Weight:{self.weight}kg - Delivery Status:{self.delivery_status}"

    def update_status(self, status):
        self.delivery_status = status

    def update_time(self, time):
        self.delivery_time = time

    def update_address(self,new_address):
        self.address = new_address

    def get_address(self):
        return self.address

    def update_left_hub_time(self, time):
        self.left_hub_time = time

    def get_left_hub_time(self):
        return self.left_hub_time

    def get_delivery_time(self):
        return self.delivery_time

    def update_truck_number(self, num):
        self.truck_number = num

    def get_truck_number(self):
        return self.truck_number

    def update_zip(self, zip):
        self.zip = zip