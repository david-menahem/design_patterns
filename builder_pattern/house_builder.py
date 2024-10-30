from builder_pattern.house import House


class HouseBuilder:
    def __init__(self):
        self.house = House()

    def set_location(self, location):
        self.house.location = location
        return self

    def set_owner(self, owner):
        self.house.owner = owner
        return self

    def set_size(self, size: int):
        self.house.size = size
        return self

    def set_year(self, year):
        self.house.year = year
        return self

    def build(self):
        return self.house