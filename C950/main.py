# Student Name: Ryan Chen
# Student ID: 012219711

import csv
import datetime

from truck import Truck
from hashmap import HashMap
from package import Package

with open("Data/address.csv") as address_csv:
    address_csv = csv.reader(address_csv)
    address_csv = list(address_csv)

with open("Data/distance.csv") as distance_csv:
    distance_csv = csv.reader(distance_csv)
    distance_csv = list(distance_csv)

with open("Data/package.csv") as package_csv:
    package_csv = csv.reader(package_csv)
    package_csv = list(package_csv)


def distance_in_between(address_1, address_2):
    distance = distance_csv[address_1][address_2]
    if distance == '':
        print("No distance")

    return float(distance)

# def greedy_algorithm(packages):

truck1 = Truck(16, 18, None, [13, 39, 14, 15, 16, 34, 19, 20, 21, 2, 33, 27, 35, 37, 40, 4], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))

truck2 = Truck(16, 18, None, [6, 25, 26, 32, 31, 28, 1, 29, 7, 30, 8, 3, 18, 36, 23, 24], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))

extra_package = [9, 5, 38, 10, 11, 12, 17, 22]
