class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, special_note, delivery_status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.special_note = special_note
        self.delivery_status = delivery_status
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip,
                                                       self.deadline, self.weight, self.special_note, self.delivery_time,
                                                       self.delivery_status)

    def update_status(self, convert_timedelta):
        if self.delivery_time < convert_timedelta:
            self.delivery_status = "Delivered"
        elif self.departure_time > convert_timedelta:
            self.delivery_status = "En route"
        else:
            self.delivery_status = "At Hub"