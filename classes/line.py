class Line:
    def __init__(self,name,origin,destination,station,station_count):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.station = station
        self.station_count = station_count

    def __str__(self):
        return f"Name: {self.name}\nOrigin: {self.origin}\nDestination: {self.destination}\nStation: {self.station}\nStation_count: {self.station_count}\n"    
        