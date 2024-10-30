class House:
    def __int__(self):
        self.location = None
        self.owner = None
        self.size = None
        self.year = None

    def __str__(self):
        return f'House: \nLocation: {self.location}, Owner: {self.owner}, Size: {self.size}, Year: {self.year}'