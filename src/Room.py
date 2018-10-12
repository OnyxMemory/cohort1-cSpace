class Room:
    def __init__(self, room_info):
        self.name, self.type, self.location, self.descriptions, self.issues = room_info
        self.rate = 0

    def add_rate(self, new_rate):
        self.rate = new_rate

    def assign_rate(self, rate_dict):
        if self.type in rate_dict.keys():
            self.add_rate(rate_dict[self.type])
        else:
            self.add_rate(0)
