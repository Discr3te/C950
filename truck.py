# Create a Truck class to store some Truck attributes
class Truck:
    def __init__(self, capacity, speed, weight, packages, mileage, address, depart_time):
        self.capacity = capacity
        self.speed = speed
        self.weight = weight
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.weight, self.packages, self.mileage,
                                               self.address, self.depart_time)