# Student Name: Ryan Chen
# Student ID: 012219711

import csv # To read CSV files
import datetime # Allow us to manipulate time

from truck import Truck
from hashmap import HashMap
from package import Package

# Read the file of address information
with open("Data/address.csv") as address_csv:
    address_csv = csv.reader(address_csv)
    address_csv = list(address_csv)

# Read the file for distance information
with open("Data/distance.csv") as distance_csv:
    distance_csv = csv.reader(distance_csv)
    distance_csv = list(distance_csv)

# Read the file for packge information
with open("Data/package.csv") as package_csv:
    package_csv = csv.reader(package_csv)
    package_csv = list(package_csv)

# Function to find the distance between two addresses
def distance_in_between(address_1, address_2):
    distance = distance_csv[address_1][address_2]
    if distance == '':
        distance = distance_csv[address_2][address_1]

    return float(distance)

# Given a string literal of address, it find the number associated with the address
def extract_address(address):
    for row in address_csv:
        if address in row[2]:
            return int(row[0])

# Using csv.reader it goes through and parses the information
# Loads package data into hash table
def load_package_data(filename, package_hash):
    with open(filename) as package_csv:
        package_csv = csv.reader(package_csv)
        for row in package_csv:
            id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            deadline = row[5]
            weight = int(row[6])
            special_note = row[7]
            delivery_status = "At Hub or waiting for arrival"

            package_detail = Package(id, address, city, state, zip, deadline, weight, 
                              special_note, delivery_status)

            package_hash.insert(id, package_detail)

# Using greedy algo to sort the packages load onto to truck and find the shortest path.
def greedy_algorithm_delivery(truck):
    # Places all the packages in a empty array
    original_set = []
    for packageID in truck.packages:
        package = package_hash.search(packageID)
        original_set.append(package)

    # Clear all the packages in the truck, so we can put the sorted packages back into the truck
    truck.packages.clear()

    # Cycles throguth the original set array until 0 packages are left
    while len(original_set) > 0:
        closest_package = None
        shortest_distance = float("inf")

        for package in original_set:
            dist = distance_in_between(extract_address(truck.address), extract_address(package.address))
            if  dist <= shortest_distance:
                shortest_distance = dist
                closest_package = package
        if closest_package:
            # Adds the closest package to the truck.package list
            truck.packages.append(closest_package.id)

            # Remove the closest package from the origainl set so we don't use it again
            original_set.remove(closest_package)

            # Add the mileage driven to the closest package to truck mileage
            truck.mileage += shortest_distance

            # Add the weight of the closest package to the truck weight
            truck.weight += closest_package.weight

            # set the truck address to the closest package to indicate that the truck drove to the closest package and is now at the closest package location
            truck.address = closest_package.address

            # Update the time it took for the truck to drive to the nearest package
            truck.time += datetime.timedelta(hours=shortest_distance / 18)

            # Update the packages delivery time
            closest_package.delivery_time = truck.time
            closest_package.departure_time = truck.time
    
    # This if statement checks if the package list is from truck 2 (first trip). 
    # If it is then it take the trucks current location which is going to be the last package delivered location and find the distance between it and the 
    # HUB to indicate the truck has to go back to the HUB and pick up the rest of the packages.
    if truck2:
        dist = distance_in_between(extract_address(truck.address), extract_address("4001 South 700 East"))
        truck.mileage += dist
        truck.time += datetime.timedelta(hours=dist / 18)
    
# Create the Hash Table with 41 buckets so the package 40 doesnt go to bucket 0 since we are using MOD to generate the hash key.
package_hash = HashMap(41)

# Load packages into hash table
load_package_data("Data/package.csv", package_hash)

# Pre loaded package list
set1 = [13, 39, 14, 15, 16, 34, 19, 20, 21, 2, 33, 27, 35, 37, 40, 4]
set2 = [6, 25, 26, 32, 31, 28, 1, 29, 7, 30, 8, 3, 18, 36, 23, 10]
set3 = [9, 5, 38, 24, 11, 12, 17, 22]

# Create Truck object
truck1 = Truck(16, 18, 0, set1, 0.0, "4001 South 700 East", datetime.timedelta(hours=8))
truck2 = Truck(16, 18, 0, set2, 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))
truck2_2 = Truck(16, 18, 0, set3, 0.0, "4001 South 700 East", datetime.timedelta(hours=11, minutes=12))

# User Interface
print("WGUPS Interface")
print("---------------")
print("1. View delivery status of all packages loaded onto each truck at a timeframe.")
print("2. View delivery status of all packages at a specific time.")
print("3. Exit")
choice = input("Enter 1 or 2 to proceed: ") # Ask the user to input either 1 or 2 to continue with the program

# Converting the trucks depart time to a variable that allows us to compare the times
truck1_depart_time = datetime.datetime.strptime("8:00", "%H:%M")
truck2_depart_time = datetime.datetime.strptime("9:05", "%H:%M")
# Initiating the variable total miles traveled to use in printing out the trucks miles traveled
total_miles_traveled = 0

# If user chose 1
if choice == '1':

    # User asked to enter the first time
    print("Use 24 hour format.")
    first_input = input("Enter start time (HH:MM): ")
    (h1, m1) = first_input.split(":")
    convert_timedelta1 = datetime.timedelta(hours=int(h1), minutes=int(m1))

    # User asked to enter the second time
    second_input = input("Enter end time (HH:MM): ")
    (h2, m2) = second_input.split(":")
    convert_timedelta2 = datetime.timedelta(hours=int(h2), minutes=int(m2))


    # Converting the input times to variables that allows us to compare the times
    first_time = datetime.datetime.strptime(first_input, "%H:%M")
    second_time = datetime.datetime.strptime(second_input, "%H:%M")
    
    # Converting the trucks depart time to a variable that allows us to compare the times
    truck1_depart_time = datetime.datetime.strptime("8:00", "%H:%M")
    truck2_depart_time = datetime.datetime.strptime("9:05", "%H:%M")
    # Initiating the variable total miles traveled to use in printing out the trucks miles traveled
    total_miles_traveled = 0

    # If the time when package #9 address is updated is in between the timeframe given or the first time is greater than the package update time, the package #9 address will update
    update_wrong_address_time = datetime.datetime.strptime("10:20", "%H:%M")
    if first_time <= update_wrong_address_time <= second_time or first_time >= update_wrong_address_time:
        fixed_address = Package(9,"410 S State St","Salt Lake City","UT","84111","EOD",2,"Wrong address updated at 10:20","At Hub or waiting for arrival")
        package_hash.insert(9, fixed_address)

    # The following 3 if statements check if the trucks departure time is in between the first and second time or before the first time.
    # If it is then it will run the algorithm and print out the package in order of delivery, else it will still print it out but to indicate that the packages is still at the HUB
    if first_time <= truck1_depart_time <= second_time or truck1_depart_time <= first_time:
        greedy_algorithm_delivery(truck1)
        print("Truck 1 Packages")
        print("ID, Address, City, State, Zip, Deadline, Weight, Special Note, Delivery Time, Delivery Status")
        # For every package it calls the update_status method to change if the package is "Delivered", "En route", or "At Hub".
        # Also prints out all the package information
        for packageID in truck1.packages:
            package = package_hash.search(packageID)
            package.update_status(convert_timedelta1)
            print(str(package))
    else: # Prints out the packages that still is at the hub
        print("\n")
        greedy_algorithm_delivery(truck2_2)
        print("Truck 2 Pakcages (Second Trip)")
        print("ID, Address, City, State, Zip, Deadline, Weight, Special Note, Delivery Time, Delivery Status")
        for packageID in truck2_2.packages:
            package = package_hash.search(packageID)
            print(str(package))

    # The code below is a carbon copy of the code above, only changing the truck variable and using convert_timedelta2
    if first_time <= truck2_depart_time <= second_time or truck2_depart_time <= first_time:
        print("\n")
        greedy_algorithm_delivery(truck2)
        print("Truck 2 Packages")
        print("ID, Address, City, State, Zip, Deadline, Weight, Special Note, Delivery Time, Delivery Status")
        for packageID in truck2.packages:
            package = package_hash.search(packageID)
            package.update_status(convert_timedelta2)
            print(str(package))
    else: # Prints out the packages that still is at the hub
        print("\n")
        greedy_algorithm_delivery(truck2_2)
        print("Truck 2 Pakcages (Second Trip)")
        print("ID, Address, City, State, Zip, Deadline, Weight, Special Note, Delivery Time, Delivery Status")
        for packageID in truck2_2.packages:
            package = package_hash.search(packageID)
            print(str(package))  

    # Makes sure truck2 (second trip) only goes when truck 2 (first trip) is back
    truck2_2.depart_time = truck2.time
    truck2_2.time = truck2.time
    truck2_2_depart_time = datetime.datetime.strptime(str(truck2_2.depart_time), "%H:%M:%S")

    if first_time <= truck2_2_depart_time <= second_time or truck2_2_depart_time <= first_time:
        print("\n")
        greedy_algorithm_delivery(truck2_2)
        print("Truck 2 Pakcages (Second Trip)")
        print("ID, Address, City, State, Zip, Deadline, Weight, Special Note, Delivery Time, Delivery Status")
        for packageID in truck2_2.packages:
            package = package_hash.search(packageID)
            package.update_status(convert_timedelta2)
            print(str(package))
    else: # Prints out the packages that still is at the hub
        print("\n")
        greedy_algorithm_delivery(truck2_2)
        print("Truck 2 Pakcages (Second Trip)")
        print("ID, Address, City, State, Zip, Deadline, Weight, Special Note, Delivery Time, Delivery Status")
        for packageID in truck2_2.packages:
            package = package_hash.search(packageID)
            print(str(package))

    print("\n")
    print(f"Total Miles Traveled By All Trucks: {truck1.mileage + truck2.mileage + truck2_2.mileage}")

elif choice == '2':
    print("Use 24 hour format.")
    first_input = input("Enter time (HH:MM): ")
    (h1, m1) = first_input.split(":")
    convert_timedelta1 = datetime.timedelta(hours=int(h1), minutes=int(m1))
    first_time = datetime.datetime.strptime(first_input, "%H:%M")

    # If the time given is >= 10:20, then the package #9 address will update
    update_wrong_address_time = datetime.datetime.strptime("10:20", "%H:%M")
    if first_time >= update_wrong_address_time:
        fixed_address = Package(9,"410 S State St","Salt Lake City","UT","84111","EOD",2,"Wrong address updated at 10:20","At Hub or waiting for arrival")
        package_hash.insert(9, fixed_address)

    # The following three if statements check if the time entered is greater than or equal to the trucks departure time.
    # If it is then it will run the greedy algorithm and update the package status if its delivered at or after the first time
    # else it still prints out the packages without updated package status to indicate that the packages are still at the HUB or waiting for the package to get there
    if first_time >= truck1_depart_time:
        greedy_algorithm_delivery(truck1)
        print("Truck 1 Packages")
        print("ID, Address, City, State, Zip, Deadline, Weight, Special Note, Delivery Time, Delivery Status")
        # For every package it calls the update_status method to change if the package is "Delivered", "En route", or "At Hub".
        # Also prints out all the package information
        for packageID in truck1.packages:
            package = package_hash.search(packageID)
            package.update_status(convert_timedelta1)
            print(str(package))
    else: # Prints out the packages that still is at the hub
        print("\n")
        greedy_algorithm_delivery(truck2_2)
        print("Truck 2 Pakcages (Second Trip)")
        print("ID, Address, City, State, Zip, Deadline, Weight, Special Note, Delivery Time, Delivery Status")
        for packageID in truck2_2.packages:
            package = package_hash.search(packageID)
            print(str(package))

    # The code below is a carbon copy of the code above, only changing the truck variable and using convert_timedelta2
    if first_time >= truck2_depart_time:
        print("\n")
        greedy_algorithm_delivery(truck2)
        print("Truck 2 Packages")
        print("ID, Address, City, State, Zip, Deadline, Weight, Special Note, Delivery Time, Delivery Status")
        for packageID in truck2.packages:
            package = package_hash.search(packageID)
            package.update_status(convert_timedelta1)
            print(str(package))
    else: # Prints out the packages that still is at the hub
        print("\n")
        greedy_algorithm_delivery(truck2_2)
        print("Truck 2 Pakcages (Second Trip)")
        print("ID, Address, City, State, Zip, Deadline, Weight, Special Note, Delivery Time, Delivery Status")
        for packageID in truck2_2.packages:
            package = package_hash.search(packageID)
            print(str(package))  

    # Makes sure truck2 (second trip) only goes when truck 2 (first trip) is back
    truck2_2.depart_time = truck2.time
    truck2_2.time = truck2.time
    truck2_2_depart_time = datetime.datetime.strptime(str(truck2_2.depart_time), "%H:%M:%S")

    if first_time >= truck2_2_depart_time:
        print("\n")
        greedy_algorithm_delivery(truck2_2)
        print("Truck 2 Pakcages (Second Trip)")
        print("ID, Address, City, State, Zip, Deadline, Weight, Special Note, Delivery Time, Delivery Status")
        for packageID in truck2_2.packages:
            package = package_hash.search(packageID)
            package.update_status(convert_timedelta1)
            print(str(package))
    else: # Prints out the packages that still is at the hub
        print("\n")
        greedy_algorithm_delivery(truck2_2)
        print("Truck 2 Pakcages (Second Trip)")
        print("ID, Address, City, State, Zip, Deadline, Weight, Special Note, Delivery Time, Delivery Status")
        for packageID in truck2_2.packages:
            package = package_hash.search(packageID)
            print(str(package))

    print("\n")
    print(f"Total Miles Traveled By All Trucks: {truck1.mileage + truck2.mileage + truck2_2.mileage}")

# If the user enters 2 then the program will terminate.
elif choice == '3':
    print("Exiting...")
    exit()
# If the user inputs a number other than 1 or 2 then the program will print out the statement and terminate
else:
    print("Invalid input. Please enter 1 or 2.")
