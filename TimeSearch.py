import Package
from datetime import time
import HashTable

def update_status(package_id, time1, hash_table):
    time_check = time1
    en_route_time = (hash_table.search(package_id)).get_left_hub_time()
    delivery_time = (hash_table.search(package_id)).get_delivery_time()
    truck_num = (hash_table.search(package_id)).get_truck_number()
    if time_check < en_route_time:
        (hash_table.search(package_id)).update_status("Package has not yet left the hub.")
    elif time_check < delivery_time:
        (hash_table.search(package_id)).update_status(f"Package En Route on truck #{truck_num}")
    elif time_check >= delivery_time:
        (hash_table.search(package_id)).update_status(f"Package Delivered by Truck #{truck_num} at {delivery_time}")
    if package_id == 9:
        u_time = time((10),(20))
        if time_check >= u_time:
            (hash_table.search(9)).update_address("410 S. State St.")
            (hash_table.search(9)).update_zip(84111)
        if time_check < u_time:
            (hash_table.search(9)).update_address("300 State St")
            (hash_table.search(9)).update_zip(84103)