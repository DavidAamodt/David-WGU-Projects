# DavidAamodt studentID-003303454 NHP3 TASK 2
import Package
import HashTable
import Truck
import DataImport
from datetime import time
import TimeSearch

#creates hash table and populates it with package id, package object pairs
hash_table = HashTable.HashTable()
DataImport.insert(hash_table)
#package groups to be loaded onto trucks
load1 = [1, 2, 4, 12, 13, 14, 15, 16, 19, 20, 21, 29, 30, 33, 34, 37]
load2 = [3, 5, 6, 11, 17, 18, 22, 23, 25, 26, 31, 32, 36, 38, 39, 40]
load3 = [7, 8, 9, 10, 24, 27, 28, 35]
#creates 3 truck objects
truck1 = Truck.Truck(1)
truck2 = Truck.Truck(2)
truck3 = Truck.Truck(3)
#loads each of the trucks inventory's with their assigned load
truck1.load(load1)
truck2.load(load2)
truck3.load(load3)
#starting at the given time and address(hub), each truck delivers all packages in their inventory while updating mileage and package data in the hash table
truck1.deliver(start_address= "4001 South 700 East", start_time= time((8),(0)), hash_table= hash_table)
truck2.deliver(start_address= "4001 South 700 East", start_time= time((9),(6)), hash_table= hash_table)
truck3.deliver(start_address= "4001 South 700 East", start_time= time((10),(21)), hash_table= hash_table)

#as long as input is not exit, the program runs
input1 = input("To view package data, enter \'package\' - To view truck mileage, enter \'mileage\' - To exit, enter \'exit\'\n")
while(input1 != "exit"):
    #if input is package, options to view one or all packages are given
    if input1 == "package":
        package_input = input("To view one package at a given time, type \'single\' - To view all packages at a given time, type \'all\' - To return to menu, enter \'back\' \n")
        while package_input != "back":
            if package_input == "single":
                single_input = input("Please enter the package id of the package you would like to view (example: 14) \n")
                time_input = input("Please enter the time you would like to check on the given package (example: 11:35) \n")
                try:
                    t1 = time_input.split(":")
                    input_hour = int(t1[0])
                    input_min = int(t1[1])
                    input_time = time((input_hour), (input_min))
                    input_id = int(single_input)
                    if input_id < 41:
                        TimeSearch.update_status(input_id, input_time, hash_table)
                        print(hash_table.search(input_id))
                    else:
                        print("Package not found, please try again \n")
                    print("\n")
                except ValueError or IndexError:
                    print("Invalid value entered, please try again \n")
                package_input = input("To view one package at a given time, type \'single\' - To view all packages at a given time, type \'all\' - To return to menu, enter \'back\' \n")
            elif package_input == "all":
                all_input = input("Please enter the time you would like to view all packages (example: 11:35) \n")
                try:
                    t1 = all_input.split(":")
                    input_hour = int(t1[0])
                    input_min = int(t1[1])
                    input_time = time((input_hour), (input_min))
                    i = 1
                    while i < 41:
                        TimeSearch.update_status(i, input_time, hash_table)
                        print(hash_table.search(i))
                        i += 1
                    print("\n")
                except ValueError or IndexError:
                    print("Invalid value entered, please try again \n")
                package_input = input("To view one package at a given time, type \'single\' - To view all packages at a given time, type \'all\' - To return to menu, enter \'back\' \n")
            else:
                print("Incorrect command entered. Please try again")
                package_input = input("To view one package at a given time, type \'single\' - To view all packages at a given time, type \'all\' - To return to menu, enter \'back\' \n")
        input1 = input("To view package data, enter \'package\' - To view truck mileage, enter \'mileage\' - To exit, enter \'exit\'\n")
    #if input is mileage, truck reports and mileage are given
    elif input1 == "mileage":
        mileage_input = None
        while mileage_input != "back":
            print(truck1.report)
            print(truck2.report)
            print(truck3.report)
            print(f"Total Miles =", truck1.miles + truck2.miles + truck3.miles)
            print("\n")
            mileage_input = input("To return to menu, enter \'back\' \n")
        input1 = input("To view package data, enter \'package\' - To view truck mileage, enter \'mileage\' - To exit, enter \'exit\'\n")
    #if command is not recognized, user is prompted to try again
    else:
        print("Incorrect command entered. Please try again")
        input1 = input("To view package data, enter \'package\' - To view truck mileage, enter \'mileage\' - To exit, enter \'exit\'\n")


print("Goodbye!")